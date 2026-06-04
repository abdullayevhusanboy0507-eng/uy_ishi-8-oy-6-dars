from django.contrib import admin

from .models import Genre, Director, Movie, Comment


admin.site.register([Genre, Director, Movie, Comment])
