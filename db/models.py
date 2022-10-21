from django.db import models
from datetime import datetime


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
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="actors")
    genres = models.ManyToManyField(Genre, related_name="genres")

    def __str__(self) -> str:
        return f"{self.title}"


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

    # @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(
        CinemaHall,
        related_name="cinema_hall",
        null=True,
        on_delete=models.SET_NULL
    )
    movie = models.ForeignKey(
        Movie,
        related_name="movie",
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return f"{self.movie} " + \
               datetime.strftime(self.show_time, "%Y-%m-%d %H:%M:%S")
