from django.shortcuts import render
from rest_framework import viewsets
from db.models import Film, Rate, Comment, SubComment
from movies.serializers import FilmSerializer

# Create your views here.
class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
