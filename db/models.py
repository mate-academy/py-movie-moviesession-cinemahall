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
    title = models.CharField(max_length=255, verbose_name="Назва фільму")
    description = models.TextField(verbose_name="Опис")
    actors = models.ManyToManyField(Actor, related_name="movies", verbose_name="Актори")
    genres = models.ManyToManyField(Genre, related_name="movies", verbose_name="Жанри")

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва кінозалу")
    rows = models.IntegerField(verbose_name="Кількість рядів")
    seats_in_row = models.IntegerField(verbose_name="Кількість місць у ряду")

    def __str__(self):
        return f"{self_name}"

    @property
    def capacity(self):
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    show_time = models.DateTimeField(verbose_name="Дата та час показу фільму")
    cinema_hall = models.ForeignKey("CinemaHall", on_delete=models.CASCADE, related_name="MovieSessions", verbose_name="Кінозал")
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="movie_sessions", verbose_name="Фільм")

    def __str__(self) -> str:
        formatted_time=timezone.localtime(timezone.now()).strftime("%Y/%m/%d %H:%M:%S")
        return f"{self.movie.title}{formatted_time}"


