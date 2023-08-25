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
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(
        to="Actor",
        related_name="movies"
    )
    genres = models.ManyToManyField(
        to="Genre",
        related_name="genres"
    )

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(
        to="CinemaHall",
        related_name="movie_sessions",
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        to="Movie",
        related_name="movie_sessions",
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.movie.title} {self.show_time}"
