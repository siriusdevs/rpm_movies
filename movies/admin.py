"""Admin module for registering models in admin panel."""
from django.contrib import admin
from .models import Genre, Person, Filmwork, PersonFilmwork, GenreFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Register Genre Admin Model."""

    model = Genre


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Register Person Admin Model."""

    model = Person


@admin.register(PersonFilmwork)
class PersonFilmworkInline(admin.ModelAdmin):
    """Register PersonFilmwork Admin Model."""

    model = PersonFilmwork


@admin.register(GenreFilmwork)
class GenreFilmworkInline(admin.ModelAdmin):
    """Register GenreFilmwork Admin Model."""

    model = GenreFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    """Register Filmwork Admin Model."""

    # inlines = (GenreFilmwork,)

    list_display = ('title', 'type', 'creation_date', 'rating')

    list_filter = ('type',)

    search_fields = ('title', 'description', 'rating')
