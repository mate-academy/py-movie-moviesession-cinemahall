from django.db import models
from django.db.models import SET_NULL


class Genre(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    objects = models.Manager
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    objects = models.Manager
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    objects = models.Manager
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(
        CinemaHall,
        on_delete=SET_NULL,
        null=True,
        related_name="movie_sessions"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=SET_NULL,
        null=True,
        related_name="movie_sessions"
    )

    def __str__(self) -> str:
        return (f"{self.movie.title} "
                f"{self.show_time.strftime('%Y-%m-%d %H:%M:%S')}")
