"""Urls for movies app, used in settings/urls."""
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Filmwork', views.FilmworkViewSet)
router.register(r'Genre', views.GenreViewSet)
router.register(r'Person', views.PersonViewSet)
router.register(r'GenreFilmwork', views.GenreFilmworkViewSet)
router.register(r'PersonFilmwork', views.PersonFilmworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
