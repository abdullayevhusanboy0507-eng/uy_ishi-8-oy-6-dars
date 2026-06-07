from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from .models import Genre, Director, Movie, Comment
from .serializers import GenreSerializer, DirectorSerializer, MovieSerializer, CommentSerializer
from .permissions import MyAuthenticatedOrReadOnly, CommentAuthenticatedOrReadOnly

class GenreAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'genre_id'
    permission_classes = permissions.DjangoModelPermissionsOrAnonReadOnly
    
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
    permission_classes = [MyAuthenticatedOrReadOnly, CommentAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(movie_id=self.kwargs.get('movie_id'))
    
    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_id'))
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['movie'] = movie
        serializer.save()
        return serializer
    
class CommentRetreveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'comment_id'
    permission_classes = [MyAuthenticatedOrReadOnly, CommentAuthenticatedOrReadOnly]