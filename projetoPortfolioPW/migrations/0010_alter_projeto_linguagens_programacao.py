# Generated by Django 4.0.6 on 2024-04-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoPortfolioPW', '0009_remove_linguagemprogramacao_projeto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='linguagens_programacao',
            field=models.ManyToManyField(blank=True, null=True, to='projetoPortfolioPW.linguagemprogramacao'),
        ),
    ]
