from datetime import datetime

from django.db import models


class Genre(models.Model):
    name: str = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name: str = models.CharField(max_length=255)
    last_name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title: str = models.CharField(max_length=255)
    description: str = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name: str = models.CharField(max_length=255)
    rows: int = models.IntegerField()
    seats_in_row: int = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class MovieSession(models.Model):
    show_time: datetime = models.DateTimeField()
    cinema_hall: CinemaHall = models.ForeignKey(
        CinemaHall,
        on_delete=models.CASCADE
    )
    movie: Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        show_time = self.show_time.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.movie.title} {show_time}"
