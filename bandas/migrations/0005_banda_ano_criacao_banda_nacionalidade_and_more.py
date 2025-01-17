# Generated by Django 4.0.6 on 2024-04-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_alter_album_capa_alter_banda_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='ano_criacao',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='duracao_musica',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='ano',
            field=models.IntegerField(null=True),
        ),
    ]
