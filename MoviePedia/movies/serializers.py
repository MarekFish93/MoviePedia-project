from rest_framework import serializers
from db.models import Film, Rate, Comment, SubComment

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year', 'genre', 'director','plot','runtime')
        
