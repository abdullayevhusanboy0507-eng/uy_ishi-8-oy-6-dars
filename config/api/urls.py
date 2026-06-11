from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path, include

from .views import *

router = DefaultRouter()
router.register('genres',GenreAPIViewSet,basename='genres')
router.register('directors',DirectorAPIView,basename='directors')
router.register('movie',MovieAPIView,basename='movie')


urlpatterns = [
    path('', include(router.urls)),
    path('movie/<int:movie_id>/comment/', CommentAPIView.as_view({'get':'list','post':'create'})),
    path('movie/<int:movie_id>/comment/<int:comment_id>/', CommentAPIView.as_view({'get':'retrieve','put':'update',
                                                           'patch':'partial_update','delete':'destroy'})),
]


