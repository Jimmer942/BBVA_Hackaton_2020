import tweepy
import os

key = os.getenv('key')
secret_key = os.getenv('secret_key')
token = os.getenv('token')
secret_token = os.getenv('secret_token')
print(secret_token)
auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(token, secret_token)

api = tweepy.API(auth)

user = api.me()

print(user.name)

tweets = list()

tweets.extend(api.user_timeline(screen_name='bbva', count=5, page=1, tweet_mode='extended'))
print(tweets)
print('NUmero: ', len(tweets))
print('Tweets cuenta de BBVA:')
for i in tweets:
    print('*', i.full_text)


print('\n Tweets mencion de BBVA:')
def get_all_realted_tweets():

    tt = list()
    tt.extend(api.search(q='bbva', count=5, tweet_mode='extended'))
    # print(tt.__dict__)
    for t in tt:
        t.author = t.user.escreen_name
        t.location = t.user.location
    return tt
