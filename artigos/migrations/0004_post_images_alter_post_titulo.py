# Generated by Django 4.0.6 on 2024-03-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0003_rename_post_rating_post_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
