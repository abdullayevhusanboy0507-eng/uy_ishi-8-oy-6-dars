from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Director(models.Model):
    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='uzbekistan')
    description = models.TextField(null=True, blank=True)
     
    def __str__(self):
        return self.full_name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    year = models.DateField()
    genres = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    
    
    def __str__(self):
        return self.comment