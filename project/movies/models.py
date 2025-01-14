from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='movie_genre', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    # def movie_genres(self):
    #     return 
    

class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']
