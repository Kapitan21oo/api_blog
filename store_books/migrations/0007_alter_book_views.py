# Generated by Django 4.2 on 2023-04-29 18:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_books', '0006_book_views_alter_book_author_review_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='views',
            field=models.ManyToManyField(related_name='views_book', through='store_books.UserBookRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
