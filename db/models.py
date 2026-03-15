from django.db import models
from db.models import Actor, Genre  # assuming these exist


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def capacity(self):
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} {self.show_time}"
