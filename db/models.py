from django.db import models
from django.db.models import ManyToManyField, ForeignKey
from django.db.models import TextField, IntegerField, DateTimeField, CharField


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = CharField(max_length=255)
    description = TextField()
    actors = ManyToManyField(Actor, related_name="movies")
    genres = ManyToManyField(Genre, related_name="movies")

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = CharField(max_length=255)
    rows = IntegerField()
    seats_in_row = IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class MovieSession(models.Model):
    show_time = DateTimeField()
    cinema_hall = ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"{self.movie.title} "
                f"{self.show_time.strftime('%Y-%m-%d %H:%M:%S')}")
