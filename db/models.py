from django.db import models
from django.db.models import CharField


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> CharField:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> CharField:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField(null=True)
    seats_in_row = models.IntegerField(null=True)

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> CharField:
        return self.name


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie.title} " \
               f"{self.show_time.strftime('%Y-%m-%d %H:%M:%S')}"
