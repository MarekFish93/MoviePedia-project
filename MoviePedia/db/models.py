from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length = 264)
    year = models.IntegerField(validators = [
                            MinValueValidator(1800),
                            MaxValueValidator(2030)
                            ]
    )
    genre = models.CharField(max_length = 60)
    director = models.CharField(max_length = 60)
    plot = models.CharField(max_length = 600)
    runtime = models.IntegerField(validators = [
                            MinValueValidator(1),
                            MaxValueValidator(1000)
                            ]
    )

class Rate(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE)
    rate_value = models.IntegerField(validators = [
                            MinValueValidator(1),
                            MaxValueValidator(10)
                            ]
    )

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE)
    comment_content = models.CharField(max_length = 500)

class SubComment(models.Model):
    comment_index = models.ForeignKey(Comment, on_delete = models.CASCADE)
    subcomment_content = models.CharField(max_length = 500)
