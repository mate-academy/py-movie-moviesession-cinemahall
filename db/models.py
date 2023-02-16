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
        Actor,
        related_name="movies"
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="genres"

    )

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return f"{self.name}"


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(
        CinemaHall,
        on_delete=models.CASCADE,
        related_name="cinema_halls"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    def __str__(self) -> str:
        year = self.show_time.year
        month = self.show_time.month
        day = self.show_time.day
        hour = self.show_time.hour
        minute = self.show_time.minute
        return f"{self.movie.title} " \
               f"{year}-{month:02}-{day:02} " \
               f"{hour:02}:{minute:02}:00"
