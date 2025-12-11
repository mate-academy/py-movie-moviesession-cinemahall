# db/models.py

from django.db import models


class Actor(models.Model):
    """Model reprezentujący aktora."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    """Model reprezentujący gatunek filmowy."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Model reprezentujący film."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Zmieniono z "Actor" na Actor i z "Genre" na Genre,
    # ponieważ klasy są teraz zdefiniowane w tym samym pliku.
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        """Implementacja string representation dla Movie: Speed"""
        return self.title


class CinemaHall(models.Model):
    """Model reprezentujący salę kinową."""
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        """Właściwość zwracająca całkowitą liczbę miejsc w sali."""
        return self.rows * self.seats_in_row

    def __str__(self):
        """Implementacja string representation dla CinemaHall: Blueprint"""
        return self.name


class MovieSession(models.Model):
    """Model reprezentujący seans filmowy."""
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(
        CinemaHall, on_delete=models.CASCADE, related_name="movie_sessions"
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_sessions"
    )

    def __str__(self):
        """Implementacja string representation dla MovieSession: Speed 2021-11-29 16:40:00"""
        return f"{self.movie.title} {self.show_time.strftime('%Y-%m-%d %H:%M:%S')}"
