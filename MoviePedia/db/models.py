from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


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

    @property
    def avg_rating(self):
        ratings = self.ratings.all().values_list('rate_value')
        if ratings:
            avg = sum(sum(x) for x in ratings)/len(ratings)
            return round(avg, 2)
        else:
            return 'not found'


    def __str__(self):
        return self.title

class Rate(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE, related_name = 'ratings')
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
    related_to = models.ForeignKey('self',related_name = "subcomments",on_delete = models.CASCADE, blank = True, null=True)

    class Meta:
        ordering = ['add_date']

    def __str__(self):
        return str(self.comment_content[:15])
