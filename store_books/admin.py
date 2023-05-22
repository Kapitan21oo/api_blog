from django.contrib import admin

from store_books.models import Category, Book, Author

# Register your models here.


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)
