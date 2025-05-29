from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(name: str,
                       rows: int,
                       seats_in_row: int
                       ) -> None:
    CinemaHall.objects.create(
        hall_name=name,
        hall_rows=rows,
        hall_seats_in_row=seats_in_row
    )
