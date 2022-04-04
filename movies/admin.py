from django.contrib import admin
from .models import Genre, Person, Filmwork, PersonFilmwork, GenreFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonFilmwork)
class PersonFilmworkInline(admin.ModelAdmin):
    model = PersonFilmwork
    
@admin.register(GenreFilmwork)
class GenreFilmworkInline(admin.ModelAdmin):
    model = GenreFilmwork

@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    #inlines = (GenreFilmwork,)

    list_display = ('title', 'type', 'creation_date', 'rating')

    list_filter = ('type',)

    search_fields = ('title', 'description', 'rating')