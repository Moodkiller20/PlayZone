# Generated by Django 4.1.4 on 2023-01-13 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayZoneGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('url_link', models.URLField(blank=True, max_length=60, null=True)),
                ('img_profile', models.ImageField(blank=True, default=None, null=True, upload_to='Game_profile/')),
            ],
        ),
    ]
