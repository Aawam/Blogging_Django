# Generated by Django 5.0.4 on 2024-04-29 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog_article',
            options={'ordering': ['title']},
        ),
    ]