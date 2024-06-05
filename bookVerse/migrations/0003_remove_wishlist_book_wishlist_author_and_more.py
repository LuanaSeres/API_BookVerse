# Generated by Django 5.0.6 on 2024-06-05 19:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookVerse', '0002_alter_book_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='book',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='author',
            field=models.CharField(default='Default Author', max_length=255),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='genre',
            field=models.CharField(default='Default Genre', max_length=100),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='title',
            field=models.CharField(default='Default Title', max_length=255),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='priority',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
