# Generated by Django 4.0.6 on 2024-04-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetoPortfolioPW', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='semestre',
            field=models.CharField(max_length=50),
        ),
    ]
