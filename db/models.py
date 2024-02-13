from django.db import models
import datetime


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
    actors = models.ManyToManyField(Actor, related_name="Actor")
    genres = models.ManyToManyField(Genre, related_name="Genre")


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    capacity = rows * seats_in_row

    def __str__(self) -> str:
        return self.name


class CinemaSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, related_name="CinemaHall", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="Movie", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie.title} {self.show_time.strftime('%Y-%m-%d %X')}"

