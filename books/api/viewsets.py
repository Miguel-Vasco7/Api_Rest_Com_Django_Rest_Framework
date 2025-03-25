from rest_framework import viewsets
from books.api import seriallizers
from books import models

class BooksViewset(viewsets.ModelViewSet):
    serializer_class = seriallizers.BooksSerializer
    queryset = models.Books.objects.all()


    