from django.db import models

# Create your models here.
class TweetModel(models.Model):

    text = models.CharField(name='text', max_length=250)
    id = models.IntegerField()
    user = models.CharField(name='usuario', max_length=250)
    created_at = models.DateField(name='fecha_creacion') # fecha de creacion
    favorite_count = models.IntegerField(name='n_likes') # likes
    retweet_count = models.IntegerField(name='n_rt') # retweet_count
    geo = models.CharField(name='pais', max_length=250) # pais

    def __str__(self):
        return self.user

    def get_full_description(self):
        return f'user {self.user},' \
               f' text {self.text}, id {self.id},' \
               f' created_at {self.fecha}, likes {self.likes},' \
               f' retweet_count {self.retweets},' \
               f' geo {self.geo}'



