# services/cinema_hall.py

from typing import List
from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    """
    Zwraca wszystkie sale kinowe.
    """
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str,
    hall_rows: int,
    hall_seats_in_row: int
) -> CinemaHall:
    """
    Tworzy nową salę kinową.
    """
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
