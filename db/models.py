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
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    capacity = models.GeneratedField(
        expression=models.F("rows") * models.F("seats_in_row"),
        output_field=models.IntegerField(),
        db_persist=True
    )

    def __str__(self) -> str:
        return self.name


class MovieSession(models.Model):
    show_time = models.DateTimeField(null=True)
    cinema_hall = models.ForeignKey(
        CinemaHall,
        null=True,
        on_delete=models.SET_NULL
    )
    movie = models.ForeignKey(
        Movie,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return (
            f"{self.movie.title} "
            f"{self.show_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
