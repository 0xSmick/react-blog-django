from django.contrib.auth.models import User
from django.shortcuts import render
from books.serializers import *
from rest_framework import permissions, generics, viewsets, response

#from api.permissions import IsAdminOrIsTheUser
class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


