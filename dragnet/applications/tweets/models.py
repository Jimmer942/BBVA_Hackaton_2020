from django.db import models

# Create your models here.
class TweetModel(models.Model):

    text = models.CharField(max_length=250)
    id = models.IntegerField()
    usuario = models.CharField(max_length=250)
    fecha = models.DateField()
    likes = models.IntegerField()
    retweets = models.IntegerField()
    comentarios = models.IntegerField()
    pais = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

    def get_full_description(self):
        return f'nombre {self.nombre}, text {self.text}, 
        id {self.id}, usuario {self.usuario}, fecha {self.fecha},
        likes {self.likes}, retweets {self.retweets}, comentarios {self.comentarios},
        pais {self.pais}'



