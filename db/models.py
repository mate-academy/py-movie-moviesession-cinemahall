from django.db import models
from django.db.models import ManyToManyField


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
    actors = ManyToManyField(
        Actor,
        related_name="actors",
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="genres",
    )

    def __str__(self) -> str:
        return str(self.title)


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        result = self.rows * self.seats_in_row
        return result


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        new_data = self.show_time.strftime("%Y-%m-%d %H:%M:%S")
        result = self.movie.title + " " + new_data
        return result
