import tweepy
import boto3
import os
import json
import numpy as np

from .serializers import TweetSerializer
from .models import TweetModel

comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')


class Utils():
    def get_all_realted_tweets():

        key = os.getenv('key')
        secret_key = os.getenv('secret_key')
        token = os.getenv('token')
        secret_token = os.getenv('secret_token')
        auth = tweepy.OAuthHandler(key, secret_key)
        auth.set_access_token(token, secret_token)

        api = tweepy.API(auth)

        user = api.me()

        tt = list()
        result = []
        tt.extend(api.search(q='BBVA exclude:retweets', count=200, tweet_mode='extended'))
        # print(tt.__dict__)
        for t in tt:
            t.author = t.user.screen_name
            t.location = t.user.location
            data = {}
            data['author'] = t.author
            data['location'] = t.location
            data['otro'] = t.id
            data['full_text'] = t.full_text
            data['favorite_count'] = t.favorite_count
            data['retweet_count'] = t.retweet_count
            result.append(data)

        return result

    def get_sentiment(self, text):

        result = comprehend.detect_sentiment(Text=text, LanguageCode='es')
        positive = result.get('SentimentScore').get('Positive')
        negative = result.get('SentimentScore').get('Negative')
        if positive >= negative:
            return positive
        return negative*-1

    def sigmoid(self, x):

        return (2 / (1 + np.exp(-x))) - 1



