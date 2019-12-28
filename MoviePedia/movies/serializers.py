from rest_framework import serializers
from db.models import Film, Rate, Comment



# Film serializer
class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id','title', 'year', 'genre', 'director','plot','runtime')

# Rating serializers

# Serializer for rating POST
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('rate_value',)

# Serializer for rating GET
class RateMeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('avg_rating',)

# Comment serializers

# Serializer for subcomments
class SubcommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'add_date')

# Serializer for comments GET
class CommentSerializer(serializers.ModelSerializer):
    subcomments = SubcommentSerializer(read_only = 'True', many = True)
    class Meta:
        model = Comment
        fields = ('id','comment_content', 'add_date','related_to','subcomments')

# Serializer for comments POST
class CommentSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'add_date', 'related_to')
