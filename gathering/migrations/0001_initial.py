# Generated by Django 4.1.1 on 2022-09-16 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=30)),
                ('pubDate', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Searched',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('entry', models.CharField(max_length=40)),
            ],
        ),
    ]
