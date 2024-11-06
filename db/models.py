from django.db import models

from django.forms import CharField


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
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="actors")
    genres = models.ManyToManyField(Genre, related_name="genres")

    def __str__(self) -> CharField:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> CharField:
        return self.name

    @property
    def capacity(self) -> int:
        return self.seats_in_row * self.rows

class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, related_name="sessions",
                                    on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="sessions",
                              on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} {self.show_time}"
