from datetime import datetime

from django.db import models


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
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies_to_actors")
    genres = models.ManyToManyField(Genre, related_name="movies_to_genres")

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255, null=False)
    rows = models.IntegerField(null=False)
    seats_in_row = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    show_time = models.DateTimeField(null=False)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE, related_name="session_to_cinema_halls")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="session_to_movies")

    def __str__(self) -> str:
        return f"{self.movie} {self.show_time}"

