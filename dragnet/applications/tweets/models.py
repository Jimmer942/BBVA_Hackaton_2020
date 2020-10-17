from django.db import models

# Create your models here.
class TweetModel(models.Model):

    text = models.CharField(name='text', max_length=250)
    id = models.IntegerField()
    usuario = models.CharField(name='usuario', max_length=250)
    fecha = models.DateField(name='fecha_creacion')
    likes = models.IntegerField(name='n_likes')
    retweets = models.IntegerField(name='n_rt')
    comentarios = models.IntegerField(name='n_comentarios')
    pais = models.CharField(name='pais', max_length=250)

    def __str__(self):
        return self.nombre

    def get_full_description(self):
        return f'nombre {self.nombre},' \
               f' text {self.text}, id {self.id},' \
               f' usuario {self.usuario},' \
               f' fecha {self.fecha}, likes {self.likes},' \
               f' retweets {self.retweets},' \
               f' comentarios {self.comentarios},pais {self.pais}'



