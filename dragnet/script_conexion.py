#!/usr/bin/python3

import tweepy


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
tt = list()
tt.extend(api.search(q='bbva', count=5, tweet_mode='extended'))
for i in tt:
    print('*', i.full_text)
print('\n END')

#print('SEARCH: ', tt[0])
#print()


#user1 = api.get_user('bbva')
#print('USER INFO')
#print(user1)
