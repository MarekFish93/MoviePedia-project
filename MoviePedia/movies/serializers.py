from rest_framework import serializers
from db.models import Film, Rate, Comment, SubComment

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id','title', 'year', 'genre', 'director','plot','runtime')

    def create(self, validated_data):
        return Film.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','comment_content')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id','rate_value')

    def create(self, validated_data):
        return Rate.objects.create(**validated_data)
