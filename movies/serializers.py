"""Module used in REST API."""
from rest_framework import serializers

from .models import Filmwork, Genre, Person, GenreFilmwork, PersonFilmwork


class FilmworkSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for REST API to Filmwork model."""

    class Meta:
        model = Filmwork
        fields = ('title', 'description', 'rating', 'type', 'creation_date', 'created')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for REST API to Genre model."""

    class Meta:
        model = Genre
        fields = ('id', 'name', 'description', 'created', 'modified')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for REST API to Person model."""

    class Meta:
        model = Person
        fields = ('full_name', 'created', 'modified')


class GenreFilmworkSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for REST API to GenreFilmwork model."""

    class Meta:
        model = GenreFilmwork
        fields = ('film_work', 'genre', 'created')


class PersonFilmworkSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for REST API to PersonFilmwork model."""

    class Meta:
        model = PersonFilmwork
        fields = ('film_work', 'person', 'role', 'created')
