from django.db import models

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField('Disciplina', related_name='docentes')

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length = 50)
    apresentacao = models.TextField(blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)
    competencias = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.PositiveSmallIntegerField()
    semestre = models.CharField(max_length=50)
    ects = models.DecimalField(max_digits=5, decimal_places=2)
    curricular_unit_readable_code = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_utilizadas = models.TextField()
    imagem = models.ImageField(upload_to='porfolioPw/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linguagens_programacao = models.ManyToManyField(LinguagemProgramacao, blank=True, null=True)