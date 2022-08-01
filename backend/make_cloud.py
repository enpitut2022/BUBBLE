# coding: UTF-8
import re
import ipadic
import subprocess
import unicodedata
import pandas as pd
import MeCab
from wordcloud import WordCloud

df = pd.read_csv("./backend/to_csv_out.csv")
df.text = df.text.str.normalize("NFKC").str.lower()
df.text = df.text.str.replace("\n", " ")
df.text = df.text.str.replace("\u2028", "")

tagger = MeCab.Tagger(ipadic.MECAB_ARGS)

kana_re = re.compile("^[ぁ-ゖ]+$")

def mecab_tokenizer(text):
    
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
    

df["tokens"] = df.text.apply(mecab_tokenizer)

text_data = " ".join(df["tokens"])

wc = WordCloud(
        font_path='./NotoSansJP-Regular.otf',
        width=600,
        height=400,
        prefer_horizontal=1.0,
        max_words=60,
        stopwords={'https','co','rt'},
        background_color='black',
        max_font_size=60,
        min_font_size=10,
        relative_scaling=0.5,
        regexp=r"\w{2,}",
        collocations=False,
        colormap='Paired',
        include_numbers=False,
        random_state=42
    ).generate(text_data)


ex_text = wc.to_svg()
print(ex_text)
wc.to_file("./backend/wc_image_ja.png")