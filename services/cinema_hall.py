from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet[CinemaHall]:
    cinema_halls = CinemaHall.objects.all()
    return cinema_halls


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> CinemaHall:
    cinema_hall = CinemaHall(name=hall_name,
                             rows=hall_rows,
                             seats_in_row=hall_seats_in_row)
    cinema_hall.save()
    return cinema_hall
