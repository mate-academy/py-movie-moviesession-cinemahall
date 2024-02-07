from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet | CinemaHall:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str = None,
        hall_rows: int = None,
        hall_seats_in_row: int = None
        ) -> CinemaHall:

    new_cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row,
    )
    return new_cinema_hall
