# Generated by Django 4.0.6 on 2024-06-10 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='portfolio/')),
                ('landing_text', models.CharField(max_length=100)),
                ('interests', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('competencies', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='portfolio/')),
                ('website_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('facebook', 'Facebook'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('other', 'Other')], max_length=50)),
                ('link', models.URLField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='portfolio.profile')),
            ],
        ),
    ]
