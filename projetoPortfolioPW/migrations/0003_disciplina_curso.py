# Generated by Django 4.0.6 on 2024-04-08 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetoPortfolioPW', '0002_alter_disciplina_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projetoPortfolioPW.curso'),
        ),
    ]
