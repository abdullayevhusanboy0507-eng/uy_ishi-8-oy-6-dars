from rest_framework import serializers

from .models import Genre, Director, Movie, Comment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        

class MovieSerializer(serializers.ModelSerializer):
    genre_write = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),)
    
    director_write = serializers.PrimaryKeyRelatedField(
        queryset=Director.objects.all(),)
    
    class Meta:
        model = Movie
        fields = ['id','name','description','yaer','genre_write','director_write']
        depth = 1
        
    
    def create(self, validated_data):
        genre_write = validated_data.pop('genre_write')
        director_write = validated_data.pop('director_write')
        movie = Movie.objects.create(genre=genre_write,
                                     director=director_write,**validated_data)
        movie.save()
        return movie
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.genre = validated_data.get('genre_write',instance.genre)
        instance.director = validated_data.get('director_write',instance.director)
        instance.save()
        return instance
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','comment','user']
        read_only_fields = ['user']