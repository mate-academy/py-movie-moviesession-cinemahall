from django.db.models import QuerySet

import init_django_orm  # noqa: F401

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    cinema_hall = CinemaHall(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )

    cinema_hall.save()
