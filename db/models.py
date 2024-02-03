from django.db import models as m


class Genre(m.Model):
    name = m.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(m.Model):
    first_name = m.CharField(max_length=255)
    last_name = m.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(m.Model):
    title = m.CharField(max_length=255)
    description = m.TextField()
    actors = m.ManyToManyField(Actor)
    genres = m.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.title


class CinemaHall(m.Model):
    name = m.CharField(max_length=255)
    rows = m.IntegerField()
    seats_in_row = m.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class MovieSession(m.Model):
    show_time = m.DateTimeField()
    cinema_hall = m.ForeignKey(CinemaHall, on_delete=m.CASCADE)
    movie = m.ForeignKey(Movie, on_delete=m.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie.title} {self.show_time}"
