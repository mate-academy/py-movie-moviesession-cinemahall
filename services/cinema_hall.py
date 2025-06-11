from django.db import models
from db.models import Genre, Movie, CinemaHall
from django.db.models.query import QuerySet


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()

def create_cinema_hall(hall_name, hall_raws, hall_seats_in_row):
    return CinemaHall(hall_name, hall_raws, hall_seats_in_row)



