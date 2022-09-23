import django.db.models.query

import init_django_orm  #noqa:F401

from db.models import CinemaHall


def get_cinema_halls():
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name, hall_rows,
                       hall_seats_in_row):
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )


if __name__ == '__main__':
    pass
