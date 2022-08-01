import tweepy
import pandas as pd
from pprint import pprint
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAGFcfQEAAAAAhOuB%2B7KYCZLDMlO62LlmkVx5q6c%3Dtkm9By2hnuq8ceehRvKgW5dtTZzpSelIxJHpVuA17aEk2gZDMN"
API_KEY="r2SZ2Pi3MKnaovR1qytC6k7HP"
API_SECRET="sUXAAqFH2F6gBgCB82E1Hx3dFpmwRGog35AbBhtAKsUVJwc0kj"
ACCESS_TOKEN="1552816814534836226-QbASXFylpCL6juhZvL9lGDSONJCg79"
ACCESS_TOKEN_SECRET="gJDS100cshsjWMKlGrVZki4Rm7N7wSF9MjBdopRDQeo6k"

# auth=tweepy.OAuthHandler(API_KEY,API_SECRET)
# auth.set_access_token(AT,AS)
# api=tweepy.API(auth)
# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    
    return client

# ★必要情報入力
search    = "死体"  # 検索対象
tweet_max = 100           # 取得したいツイート数(10〜100で設定可能)

# 関数
def SearchTweets(search,tweet_max):    
    # 直近のツイート取得
    tweets = ClientInfo().search_recent_tweets(query = search, max_results = tweet_max)

    # 取得したデータ加工
    results     = []
    tweets_data = tweets.data

    # tweet検索結果取得
    if tweets_data != None:
        for tweet in tweets_data:
            obj = {}
            obj["tweet_id"] = tweet.id      # Tweet_ID
            obj["text"] = tweet.text  # Tweet Content
            obj["author_id"] = tweet.author_id # 発信者のID
            results.append(obj)
    else:
        results.append('')
        
    # 結果出力
    return results

# 関数実行・出力
tweets = SearchTweets(search,tweet_max)
# pprint(tweets)
# result=api.home_timeline(count=3)
# for tweet in result:
#     print('ツイートID :',tweet.id)

tweet_text = []
for tweet in tweets:
    s = tweet['text'].replace('\n', '')
    tweet_text.append(s)
# pprint(tweet_text)
df = pd.DataFrame(data=tweet_text, columns=['text'])
df.to_csv('./backend/to_csv_out.csv', encoding='utf-8')