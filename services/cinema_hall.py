from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    cinema_hall = CinemaHall.objects.all()
    return cinema_hall


def create_cinema_hall(
        name: str,
        rows: int,
        seats_in_row: int
) -> CinemaHall:

    cinema_hall_create = CinemaHall.objects.create(
        name=name,
        rows=rows,
        seats_in_row=seats_in_row
    )
    return cinema_hall_create
