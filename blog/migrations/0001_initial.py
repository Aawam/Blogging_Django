# Generated by Django 5.0.6 on 2024-05-28 05:50

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Article',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
