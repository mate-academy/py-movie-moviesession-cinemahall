from django.db import models
from typing import Any


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
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    row = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.seats * self.row


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, related_name="movie_sessions",
                                    on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="movie_sessions",
                              on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"{self.movie.title} "
                f"{self.show_time.strftime('%d.%m.%Y %H:%M')}")
