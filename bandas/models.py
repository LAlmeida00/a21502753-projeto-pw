from django.db import models

# Create your models here.

class Banda(models.Model):
    foto = models.ImageField(upload_to='bandas/', null=True, blank=True)
    nome = models.CharField(max_length = 50)
    biografia = models.TextField(null=True, blank=True)
    nacionalidade = models.CharField(max_length = 50, null=True)
    ano_criacao = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete = models.CASCADE, related_name = 'albuns')
    capa =  models.ImageField(upload_to='albuns/')
    nome = models.CharField(max_length = 50)
    ano = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = 'musicas')
    nome = models.CharField(max_length = 50)
    duracao_musica = models.CharField(max_length = 10, null=True)
    spotify_link = models.URLField(max_length = 100, null=True)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.nome