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
    description = models.TextField
    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    )  # m-t-m
    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )  # m-t-m

    def __str__(self):
        return f"{self.title}"
