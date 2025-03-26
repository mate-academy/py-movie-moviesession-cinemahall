from django.conf import settings
from django.db import models
from django.utils.timezone import localtime


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
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return f"{self.title}"

class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} {self.rows} {self.seats_in_row}"

    def total_seats(self) -> int:
        return self.rows * self.seats_in_row

class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        if settings.USE_TZ:
            return f"{self.movie.title} {localtime(self.show_time).strftime('%Y-%m-%d %H:%M:%S')}"
        return f"{self.movie.title} {self.show_time.strftime('%Y-%m-%d %H:%M:%S')}"
