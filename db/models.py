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
    description = models.TextField(null=True)
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField(default=0)
    seats_in_row = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    show_time = models.DateTimeField(auto_now_add=True)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        show_time = datetime.strftime(self.show_time, "%Y-%m-%d %H:%M:%S")
        return f"{self.movie.title} {show_time}"
