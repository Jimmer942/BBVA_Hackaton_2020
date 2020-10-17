from django.db import models

# Create your models here.
class TweetModel(models.Model):

    text = models.CharField(max_length=250)
    user = models.CharField(max_length=250)
    created_at = models.DateField() # fecha de creacion
    favorite_count = models.IntegerField() # likes
    retweet_count = models.IntegerField() # retweet_count
    geo = models.CharField(max_length=250) # pais

    def __str__(self):
        return self.user

    def get_full_description(self):
        return f'user {self.user}, text {self.text}, created_at {self.created_at},
        favorite_count {self.favorite_count}, retweet_count {self.retweet_count}, geo {self.geo}'
