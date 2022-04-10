from rest_framework import serializers

from .models import Filmwork, Genre, Person, GenreFilmwork, PersonFilmwork

class FilmworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filmwork
        fields = ('title', 'description', 'rating', 
                'type', 'creation_date', 'created')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description', 'created', 'modified')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('full_name', 'created', 'modified')

class GenreFilmworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GenreFilmwork
        fields = ('film_work', 'genre', 'created')

class PersonFilmworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonFilmwork
        fields = ('film_work', 'person', 'role', 'created')