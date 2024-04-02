from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> CinemaHall:
    return CinemaHall.objects.create(name=hall_name,
                                     rows=hall_rows,
                                     seats_in_row=hall_seats_in_row)


def get_cinema_hall_by_id(cinema_hall_id: int) -> CinemaHall:
    return get_object_or_404(CinemaHall, pk=cinema_hall_id)
