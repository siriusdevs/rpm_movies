from django.contrib import admin
from .models import Genre, Person, Filmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'type', 'creation_date', 'rating')

    list_filter = ('type',)

    search_fields = ('title', 'description', 'rating')