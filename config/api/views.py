from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Genre, Director, Movie, Comment
from .serializers import GenreSerializer, DirectorSerializer, MovieSerializer, CommentSerializer


class GenreAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'genre_id'
    
    
class DirectorAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'director_id'
    

class MovieAPIView(ListCreateAPIView):
    
    def get_queryset(self):
        genre_id = self.kwargs.get('genre_id')
        if genre_id:
            return self.queryset.filter(genre_id=genre_id)
        return self.queryset.all()
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MovieSerializer
        return MovieSerializer
    

class MovieRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'  
    

class CommentAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'comment_id'