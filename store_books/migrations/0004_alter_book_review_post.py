# Generated by Django 4.2 on 2023-04-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_books', '0003_book_author_review_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review_post',
            field=models.TextField(blank=True, null=True),
        ),
    ]
