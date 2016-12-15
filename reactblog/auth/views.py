from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import UserSerializer
from rest_framework import viewsets, response, permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return response.Response(UserSerializer(request.user, context = {'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)


