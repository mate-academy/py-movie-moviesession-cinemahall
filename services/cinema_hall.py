from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_halls(
    hall_name: str,
    hall_rows: int,
    halls_seats_in_row: int
) -> CinemaHall:
    return CinemaHall.objects.create(hall_name, hall_rows, halls_seats_in_row)
