"""All apps of this django project."""
from django.apps import AppConfig


class MoviesConfig(AppConfig):
    """Explicit config for movies app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'
