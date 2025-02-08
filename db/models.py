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
    """_summary_
    -   char field title, the title of the movie with the maximum length of
        255 characters.
    -   text field description
    -   many to many field actors, which is related to the table Actor
    -   many to many field genres, which is related to the table Genre
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    """_summary_
    -   char field name, the name of the cinema hall with the maximum length
        of 255 characters
    -   integer field rows, the number of rows of seats in the hall
    -   integer field seats_in_row, the number of seats in each row
    """
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


class MovieSession(models.Model):
    """_summary_
    -   date time field show_time, the date and the time of the movie session
        performance
    -   foreign key cinema_hall, the hall where the movie session is
        performed, references to the table CinemaHall
    -   foreign key movie, the movie to be shown, references to the table Movie
    """
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.movie.title} {self.show_time}"
