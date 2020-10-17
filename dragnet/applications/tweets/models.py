from django.db import models

# Create your models here.
class TweetModel(models.Model):

    full_text = models.CharField(name='full_text', max_length=250)
    id = models.IntegerField()
    author = models.CharField(name='author', max_length=250)
    created_at = models.DateField(name='fecha_creacion') # fecha de creacion
    favorite_count = models.IntegerField(name='n_likes') # likes
    retweet_count = models.IntegerField(name='n_rt') # retweet_count
    location = models.CharField(name='pais', max_length=250) # pais

    def __str__(self):
        return self.author

    def get_full_description(self):
        return f'author {self.author},' \
               f' created_at {self.created_at}, favorite_count {self.favorite_count},' \
               f' retweet_count {self.retweet_count},' \
               f' location {self.location}'



