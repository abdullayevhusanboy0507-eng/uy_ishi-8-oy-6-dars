from rest_framework import serializers

from .models import Genre, Director, Movie, Comment


class MovieSerializerGenre(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        

class GenreSerializer(serializers.ModelSerializer):  
    movies = serializers.StringRelatedField(many=True)
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    movies = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-detail')
    movies = serializers.SlugRelatedField(many=True,read_only=True,slug_field = 'name')
    url = serializers.HyperlinkedIdentityField(view_name='genre-detail')        

    movies = MovieSerializerGenre(many=True)

    class Meta:
        model = Genre
        fields = '__all__'
        
    def create(self, validated_data):
        movies = validated_data.pop('movies')
        genre = Genre.objects.create(**validated_data)
        
        movies_list = []
        for movie in movies:
            movies_list.append(Movie(genre=genre,**movie))
        
        Movie.objects.bulk_create(movies_list)
        return genre

    
    def update(self, instance, validated_data):
        movies = validated_data.pop('movies', None)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        movies_list = []
        for movie in movies:
            movies_list.append(
                Movie(genre = instance,**movie)
            )
        Movie.objects.bulk_create(movies_list)
        return instance

class MovieSerializerDirector(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    movies = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-detail')
    movies = serializers.SlugRelatedField(many=True,read_only=True,slug_field = 'name')
    url = serializers.HyperlinkedIdentityField(view_name='director-detail') 

    movies = MovieSerializerDirector(many=True)
    
    class Meta:
        model = Director
        fields = '__all__'

    def create(self, validated_data):
        movies = validated_data.pop('movies')
        director = Director.objects.create(**validated_data)
        
        movies_list = []
        for movie in movies:
            movies_list.append(Movie(director=director,**movie))
        
        Movie.objects.bulk_create(movies_list)
        return director


    def update(self, instance, validated_data):
        movies = validated_data.pop('movies', None)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        movies_list = []
        for movie in movies:
            movies_list.append(
                Movie(genre = instance,**movie)
            )
        Movie.objects.bulk_create(movies_list)
        return instance


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
        read_only_fields = ['user21']