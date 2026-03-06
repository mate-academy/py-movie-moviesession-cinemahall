from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()

def create_cinema_hall(hall_name=None, hall_rows=None, hall_seats_in_row=None) -> QuerySet:
    create = CinemaHall.objects.create(hall_name=hall_name, hall_rows=hall_rows,
                                       hall_seats_in_row=hall_seats_in_row)
    return create