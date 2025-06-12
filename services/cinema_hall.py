import init_django_orm # noqa
from db.models import CinemaHall # noqa
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:

    new_cinema_hall = CinemaHall(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    new_cinema_hall.save()
    return new_cinema_hall
