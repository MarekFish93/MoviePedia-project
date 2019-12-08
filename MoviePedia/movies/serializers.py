from rest_framework import serializers
from db.models import Film, Rate, Comment, SubComment

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year', 'genre', 'director','plot','runtime')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','comment_content')

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id','rate_value')
