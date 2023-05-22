from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ManyToManyField(Category)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True, blank=True)
    review_post = models.TextField(blank=True, null=True)
    author_review_post = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True,
                                           related_name='author_books')

    def __str__(self):
        return str(self.id) + '. ' + self.name


