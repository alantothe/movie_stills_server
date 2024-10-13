from django.db import models

# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Movie(models.Model):
    imdb_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=200)
    date_released = models.DateField()
    imdb_rating = models.FloatField(null=True, blank=True)
    rating = models.CharField(max_length=10)
    genres = models.ManyToManyField('Genre', related_name='movies')
    directors = models.ManyToManyField(Person, related_name='directed_movies')
    cinematographers = models.ManyToManyField(Person, related_name='cinematographer_movies', blank=True)
    countries = models.ManyToManyField('Country', related_name='movies')

    def __str__(self):
        return self.title

class Still(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='stills')
    image_url = models.URLField()
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Still {self.order} for {self.movie.title}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
