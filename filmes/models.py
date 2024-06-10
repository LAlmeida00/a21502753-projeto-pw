from django.db import models

# Create your models here.

class Ator(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='filmes/', null=True, blank=True)
    atores = models.ManyToManyField(Ator, blank=True, null=True)
    generos = models.ManyToManyField(Genero, blank=True, null=True)

    def __str__(self):
        return self.nome