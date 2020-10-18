from django.db import models

# Create your models here.
class TweetModel(models.Model):

    full_text = models.CharField(max_length=350)
    otro = models.BigIntegerField()
    author = models.CharField(max_length=350)
    created_at = models.DateField(auto_now=True) # fecha de creacion
    score = models.DecimalField(default=0.0, max_digits=19, decimal_places=10)
    favorite_count = models.IntegerField() # likes
    retweet_count = models.IntegerField() # retweet_count
    location = models.CharField(max_length=350) # pais

    def __str__(self):
        return self.author

    def get_full_description(self):
        return f'author {self.author},' \
               f' created_at {self.created_at}, favorite_count {self.favorite_count},' \
               f' retweet_count {self.retweet_count},' \
               f' location {self.location}'

class DayScoreModel(models.Model):

    created_at = models.DateField(auto_now=True)
    total_score = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return f'fecha: {self.created_at}, scrore del dia: {self.total_score}'

class BestTweetModel(models.Model):

    created_at = models.DateField(auto_now=True)
    full_text = models.CharField(max_length=350)
    author = models.CharField(max_length=350)

    def __str__(self):
        return f'fecha: {self.created_at}, author: {self.author}'


class WorstTweetModel(models.Model):

    created_at = models.DateField(auto_now=True)
    full_text = models.CharField(max_length=350)
    author = models.CharField(max_length=350)

    def __str__(self):
        return f'fecha: {self.created_at}, author: {self.author}'

class TweetAnalizedModel(models.Model):

    created_at = models.DateField(auto_now=True)
    n_tweets_analized = models.IntegerField()
    n_likes_prom = models.DecimalField(max_digits=19, decimal_places=10)
    n_rt_prom = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return  f'fecha: {self.created_at} n_tweets: {self.n_tweets_analized} n_likes_prom: {self.n_likes_prom} ' \
                f'n_rt_prom: {self.n_rt_prom}'
