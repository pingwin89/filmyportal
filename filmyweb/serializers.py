from django.contrib.auth.models import User
from .models import Film
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'tytul', 'rok', 'opis', 'premiera']