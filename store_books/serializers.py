from django.db.migrations import serializer
from rest_framework.serializers import ModelSerializer

from store_books.models import Book


class BooksSerializers(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BooksSerializersView(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
