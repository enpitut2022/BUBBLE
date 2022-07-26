# coding: UTF-8
import re
import ipadic
import subprocess
import unicodedata
import pandas as pd
import MeCab
from wordcloud import WordCloud
import json
from flask import Blueprint
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__, url_prefix='/api')


class Wordcloud(Resource):

    def mecab_tokenizer(text):
        tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
        kana_re = re.compile("^[ぁ-ゖ]+$")
        
        parsed_lines = tagger.parse(text).splitlines()[:-1]
        surfaces = [l.split('\t')[0] for l in parsed_lines]
        features = [l.split('\t')[1] for l in parsed_lines]

        bases = [f.split(',')[6] for f in features]

        pos = [f.split(',')[0] for f in features]

        token_list = [b if b != '*' else s for s, b in zip(surfaces, bases)]

        target_pos = ["名詞", "動詞", "形容詞"]
        token_list = [t for t, p in zip(token_list, pos) if (p in target_pos)]

        token_list = [t for t in token_list if not kana_re.match(t)]

        token_list = [t.lower() for t in token_list]

        result = " ".join(token_list)

        result = unicodedata.normalize("NFKC", result)
        return result
    
    def make_cloud():
        df = pd.read_csv("backend/sample_data.csv")
        df.text = df.text.str.normalize("NFKC").str.lower()
        df.text = df.text.str.replace("\n", " ")
        df.text = df.text.str.replace("\u2028", "")
        df["tokens"] = df.text.apply(Wordcloud.mecab_tokenizer)

        text_data = " ".join(df["tokens"])

        wc = WordCloud(
            width=600,
            height=400,
            prefer_horizontal=0.9,
            background_color='white',
            include_numbers=False,
            colormap='tab20',
            regexp=r"\w{2,}",
            relative_scaling=1,
            collocations=False,
            max_font_size=60,
            random_state=42,
        ).generate(text_data)
        
        ex_text = wc.to_svg()
        
        tokens = df.tokens
        texts = df.text
        i = 0
        dic = {}

        for token in tokens:
            wordend = token.split()
            for word in wordend:
                dic.setdefault(word,set())
                dic[word].add(i)
            i += 1

        for key in dic.keys():
            dic[key] = list(dic[key])
        
        result = {"dic":dic,"posts":list(texts),"wordcloud":ex_text}
        ##print(json.dumps(result))
        return result

    def get(self):
        return Wordcloud.make_cloud()

api = Api(api_bp)
api.add_resource(Wordcloud, '/wcd')
