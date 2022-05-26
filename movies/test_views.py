from django.test import TestCase
from .models import Filmwork
from django.test.client import Client
from django.contrib.auth.models import User
from django.urls import reverse

OK = 200


class FilmworkListViewTest(TestCase):
    """Test for filmwork list view."""

    def setUp(self):
        """Set up client, user and create filmworks before tests."""
        self.client = Client()
        self.user = User.objects.create_user('user', 'mail@mail.com', 'itsok')
        self.client.login(username='user', password='itsok')

        number_of_filmworks = 10
        for num in range(number_of_filmworks):
            fw = 'Filmwork {0}'.format(num)
            Filmwork.objects.create(title=fw)

    def test_view_url_exists_at_desired_location(self):
        """Tests if the view exists at url."""
        resp = self.client.get('/movies/')
        self.assertEqual(resp.status_code, OK)

    def test_view_url_accessible_by_name(self):
        """Tests if the view is accessible by its name."""
        resp = self.client.get(reverse('movies'))
        self.assertEqual(resp.status_code, OK)

    def test_view_uses_correct_template(self):
        """Tests if view uses the correct template."""
        resp = self.client.get(reverse('movies'))
        self.assertEqual(resp.status_code, OK)
        self.assertTemplateUsed(resp, 'catalog/movies_page.html')
