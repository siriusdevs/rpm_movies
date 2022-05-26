"""Module for our custom tests (can be used in workflow later)."""
from django.test import TestCase
from .models import Filmwork, Person, Genre


class TestFilmworkModel(TestCase):
    """Test case for Filmwork model."""

    def test_film_work(self):
        """Creates new filmwork and tests its attributes."""
        init_kwargs = {'title': 'Title',
                       'description': 'Description',
                       'rating': 80,
                       'type': 'TV_SHOW',
                       'creation_date': '2022-05-16'
                       }
        film_work = Filmwork.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(film_work, attr), init_kwargs[attr])


class TestGenreModel(TestCase):
    """Test case for Genre model."""

    def test_genre(self):
        """Creates new genre and tests its attributes."""
        attrs = ['name', 'description']
        init_kwargs = {attr: attr.capitalize() for attr in attrs}
        genre = Genre.objects.create(**init_kwargs)
        for attr in attrs:
            self.assertEqual(getattr(genre, attr), attr.capitalize())


class TestPersonModel(TestCase):
    """Test case for Person model."""

    def test_person(self):
        """Creates new person and tests its attributes."""
        person = Person.objects.create(full_name='Full Name')
        self.assertEqual(person.full_name, 'Full Name')
