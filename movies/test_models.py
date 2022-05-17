"""Module for our custom tests (can be used in worflow later)."""
from django.test import TestCase
from .models import Filmwork, Person, Genre


class TestFilmworkModel(TestCase):
    """Test case for Filmwork model."""

    def test_film_work(self):
        """Creates new filmwork and tests its attributes."""
        attrs = ['title', 'description', 'rating', 'type', 'creation_date']
        obj_values = ['Title', 'Description', 90, 'TV_SHOW', '2022-05-16']
        init_kwargs = {}
        for attr, value in zip(attrs, obj_values):
            init_kwargs[attr] = value
        film_work = Filmwork.objects.create(**init_kwargs)
        for attr, value in zip(attrs, obj_values):
            self.assertEqual(getattr(film_work, attr), value)


class TestGenreModel(TestCase):
    """Test case for Genre model."""

    def test_genre(self):
        """Creates new genre and tests its attributes."""
        attrs = ['name', 'description']
        obj_values = ['Name', 'Description']
        init_kwargs = {}
        for attr, value in zip(attrs, obj_values):
            init_kwargs[attr] = value
        genre = Genre.objects.create(**init_kwargs)
        for attr, value in zip(attrs, obj_values):
            self.assertEqual(getattr(genre, attr), value)


class TestPersonModel(TestCase):
    """Test case for Person model."""

    def test_person(self):
        """Creates new person and tests its attributes."""
        person = Person.objects.create(full_name='Full Name')
        self.assertEqual(getattr(person, 'full_name'), 'Full Name')
