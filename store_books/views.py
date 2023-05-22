from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, generics, GenericViewSet

from store_books.models import Book
from store_books.permissions import IsOwnerOrStaffOrReadOnly
from store_books.serializers import BooksSerializers, BooksSerializersView


# Create your views here.

class ListAPIBookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializersView
    permission_classes = [AllowAny]


class ListAPIBook(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price']
    search_fields = ['author_name__name', 'name', 'category__name']  # поиск
    ordering_fields = ['price', 'author_name__name']  # сортировка

    def perform_create(self, serializer):
        serializer.validated.data['author_review_post'] = self.request.user
        serializer.save()


def oAuth(request):
    context = {
        'data': Book.objects.all()
    }

    return render(request, 'store_books/oAuth.html', context=context)



