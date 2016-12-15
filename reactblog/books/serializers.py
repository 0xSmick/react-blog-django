from rest_framework import serializers
from books.models import *
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields =('id','title','bookFile')
