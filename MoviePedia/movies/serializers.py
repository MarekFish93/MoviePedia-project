from rest_framework import serializers
from db.models import Film, Rate, Comment

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id','title', 'year', 'genre', 'director','plot','runtime')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_content','related_to', 'add_date')

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('rate_value',)
