from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: str,
                       hall_seats: str) -> None:
    CinemaHall.objects.create(name=hall_name,
                              rows=hall_rows,
                              seats=hall_seats)
