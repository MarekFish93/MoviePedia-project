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
                            ],
    )

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title

class Rate(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE)
    rate_value = models.IntegerField(validators = [
                            MinValueValidator(1),
                            MaxValueValidator(10)
                            ]
    )

    def __str__(self):
        return str(self.film.title) + str(self.rate_value)

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE)
    comment_content = models.CharField(max_length = 500)
    add_date = models.DateTimeField(auto_now=True)
    related_to = models.IntegerField(blank = True, default = None, null = True)

    class Meta:
        ordering = ['add_date']

    def __str__(self):
        return str(self.comment_content[:15])
