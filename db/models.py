from django.db import models

# (1)
class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

# (1)
class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

#  4 -> (2) < -- > 1, 1
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="actors")
    genres = models.ManyToManyField(Genre, related_name="genres")

    def __str__(self) -> str:
        return self.title

# (3) <- 4
class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row


# 3 <- (4) -> 2
class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, related_name="halls", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="movies", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f"{self.movie.title}"
                f" {self.show_time.date()}"
                f" {self.show_time.time()}")
