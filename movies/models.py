from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Genre(UUIDMixin, TimeStampedMixin):
    
    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class Person(UUIDMixin, TimeStampedMixin):

    full_name = models.CharField('full_name', max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'person'
        verbose_name_plural = 'persons'

class TypeChoices(models.TextChoices):
    MOVIE = 'MOVIE', 'movie'
    TV_SHOW = 'TV_SHOW', 'tv_show'

class Filmwork(UUIDMixin):
    
    title = models.CharField('title', max_length=255)    
    description = models.TextField('description', blank=True)
    rating = models.FloatField('rating', blank=True, \
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    type = models.CharField('type', choices=TypeChoices.choices, max_length=255)
    creation_date = models.DateField('creation_date')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'filmwork'
        verbose_name_plural = 'filmworks'
