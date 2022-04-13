"""the movies views belong here."""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Filmwork, Person, Genre, GenreFilmwork, PersonFilmwork
import movies.serializers
import os
from dotenv import load_dotenv
load_dotenv()


def custom_main(req):
    """Renders request (req) to custom index.html page.

    Args:
        req : http request.
    """
    film_works = Filmwork.objects.all().count()
    persons = Person.objects.all().count()
    genres = Genre.objects.all().count()

    return render(
        req,
        'index.html',
        context={'film_works': film_works,
                 'persons': persons,
                 'genres': genres
                 },
    )


def main_page(req):
    """Just renders main.html page.

    Args:
        req : http request.
    """
    return render(req, 'main.html')


def google_map(req):
    """Shows page with Google Map.

    Args:
        req : http request.
    """
    return render(req, 'map.html')


def mapbox_map(request):
    """Shows page with MapBox.

    Args:
        request : http request.
    """
    mapbox_access_token = os.environ.get('MAPBOX_TOKEN')
    return render(request, 'mapbox.html', {'mapbox_access_token': mapbox_access_token})


def render_dummy(req):
    """Returns simple http response.

    Args:
        req : http request.
    """
    return HttpResponse("<h1>This is the home page</h1>")


def redirection_page(req):
    """Redirects you elsewhere.

    Args:
        req : http request.
    """
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


class FilmworkViewSet(viewsets.ModelViewSet):
    """A view for FilmworkModel, all objects ordered."""

    queryset = Filmwork.objects.all().order_by('title')
    serializer_class = movies.serializers.FilmworkSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """A view for PersonModel, all objects ordered."""

    queryset = Person.objects.all().order_by('full_name')
    serializer_class = movies.serializers.PersonSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """A view for GenreModel, all objects ordered."""

    queryset = Genre.objects.all().order_by('name')
    serializer_class = movies.serializers.GenreSerializer


class GenreFilmworkViewSet(viewsets.ModelViewSet):
    """A view for GenreFilmworkModel, all objects ordered."""

    queryset = GenreFilmwork.objects.all().order_by('genre')
    serializer_class = movies.serializers.GenreFilmworkSerializer


class PersonFilmworkViewSet(viewsets.ModelViewSet):
    """A view for PersonFilmworkModel, all objects ordered."""

    queryset = PersonFilmwork.objects.all().order_by('person')
    serializer_class = movies.serializers.PersonFilmworkSerializer
