# Generated by Django 5.1.5 on 2025-02-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('body', models.TextField()),
                ('slup', models.SlugField(unique=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(related_name='posts', to='posts.tag')),
            ],
        ),
    ]
