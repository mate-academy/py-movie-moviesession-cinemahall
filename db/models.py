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

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE,
                                    null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:

        t1 = self.movie.title
        t2 = self.show_time.year

        if int(self.show_time.month) < 10:
            t3 = "0" + str(self.show_time.month)
        else:
            t3 = self.show_time.month
        if int(self.show_time.day) < 10:
            t4 = "0" + str(self.show_time.day)
        else:
            t4 = self.show_time.day
        if int(self.show_time.hour) < 10:
            t5 = "0" + str(self.show_time.hour)
        else:
            t5 = self.show_time.hour
        if int(self.show_time.minute) < 10:
            t6 = "0" + str(self.show_time.minute)
        else:
            t6 = self.show_time.minute
        if int(self.show_time.second) < 10:
            t7 = "0" + str(self.show_time.second)
        else:
            t7 = self.show_time.second

        return f"{t1} {t2}-{t3}-{t4} {t5}:{t6}:{t7}"
