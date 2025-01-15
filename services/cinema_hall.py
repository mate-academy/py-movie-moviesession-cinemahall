from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> CinemaHall:
    return CinemaHall(hall_name,
                      hall_rows,
                      hall_seats_in_row)
