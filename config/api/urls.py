from django.urls import path

from .views import *

urlpatterns = [
    path('genre/', GenreAPIView.as_view()),
    path('genre/<int:genre_id>/', GenreRetreveAPIView.as_view(),name='genre-detail'),
    path('director/', DirectorAPIView.as_view()),
    path('director/<int:director_id>/', DirectorRetreveAPIView.as_view(),name='director-detail'),
    path('movie/', MovieAPIView.as_view()),
    path('movie/<int:movie_id>/', MovieRetreveAPIView.as_view(),name='movie-detail'),
    path('movie/<int:movie_id>/comment/', CommentAPIView.as_view()),
    path('movie/<int:movie_id>/comment/<int:comment_id>/', CommentRetreveAPIView.as_view()),
]
