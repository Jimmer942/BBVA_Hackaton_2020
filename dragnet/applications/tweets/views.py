from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

from .utils import Utils
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

import  json

from .models import TweetModel, DayScoreModel, BestTweetModel, WorstTweetModel, TweetAnalizedModel
from .serializers import TweetSerializer, DayScoreSerializer, BestTweetSerializer, WorstTweetSerializer, TweetAnalizedSerializer
# Create your views here.


class TweetAllCreate(APIView):

    serializer_class = TweetSerializer

    def get(self, request, *args, **kwargs):
        data = Utils.get_all_realted_tweets()
        total_tweets_score = 0.0
        max_score = 0.0
        tweet_max_score = None
        min_score = 0.0
        tweet_min_score = None
        total_tweets = 0.0
        total_rt = 0.0
        total_likes = 0.0
        for t in data:
            tweet = TweetModel.objects.create(**t)
            score = Utils.get_sentiment(self, text=t.get('full_text'))
            print(f'score 1 {score} texto: {t.get("full_text")}')
            relevancia = tweet.retweet_count + tweet.favorite_count + 1
            score = score * relevancia
            score = Utils.sigmoid(self, x=score)
            print(f'score 2 {score}')
            tweet.score = score
            tweet.save()
            total_tweets_score = total_tweets_score + score
            total_tweets = total_tweets + 1
            total_rt = total_rt + tweet.retweet_count
            total_likes = total_likes + tweet.favorite_count
            print(f'score 3 {total_tweets_score}')
            if score > max_score:
                max_score = score
                tweet_max_score = tweet
            if score < min_score:
                min_score = score
                tweet_min_score = tweet

        DayScoreModel.objects.create(total_score=Utils.sigmoid(self, x=(total_tweets_score)))
        if tweet_max_score:
            BestTweetModel.objects.create(full_text=tweet_max_score.full_text, author=tweet_max_score.author)
        if tweet_min_score:
            WorstTweetModel.objects.create(full_text=tweet_min_score.full_text, author=tweet_min_score.author)
        rt_prom = total_rt/total_tweets
        likes_prom = total_likes/total_tweets
        TweetAnalizedModel.objects.create(n_likes_prom=likes_prom, n_tweets_analized=total_tweets, n_rt_prom=rt_prom)
        response = JsonResponse({'status': 'Ok'})
        return response


class GetBestTweetByDate(ListAPIView):

    serializer_class = BestTweetSerializer

    def get_queryset(self):
        fecha = self.kwargs.get('fecha')
        return BestTweetModel.objects.filter(
            created_at=fecha
        )


class GetWorstTweetByDate(ListAPIView):

    serializer_class = WorstTweetSerializer

    def get_queryset(self):
        fecha = self.kwargs.get('fecha')
        return WorstTweetModel.objects.filter(
            created_at=fecha
        )


class GetAnalizedTweetByDate(ListAPIView):

    serializer_class = TweetAnalizedSerializer

    def get_queryset(self):
        fecha = self.kwargs.get('fecha')
        return TweetAnalizedModel.objects.filter(
            created_at=fecha
        )

class GetDayScoreByDate(ListAPIView):

    serializer_class = DayScoreSerializer

    def get_queryset(self):
        fecha = self.kwargs.get('fecha')
        print("*****************************")
        print(fecha)
        return DayScoreModel.objects.filter(
            created_at=fecha
        )