# Generated by Django 4.0.6 on 2024-04-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_banda_ano_criacao_banda_nacionalidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='bandas/'),
        ),
    ]
