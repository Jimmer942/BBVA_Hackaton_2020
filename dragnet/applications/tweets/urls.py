from django.urls import path
from . import views

urlpatterns = [
    path('get_tweets/', views.TweetAllCreate.as_view()),
    path('get_best_tweet/<fecha>', views.GetBestTweetByDate.as_view()),
    path('get_worst_tweet/<fecha>', views.GetWorstTweetByDate.as_view()),
    path('get_analized_tweets/<fecha>', views.GetAnalizedTweetByDate.as_view()),
    path('get_day_score/<fecha>', views.GetDayScoreByDate.as_view()),
]