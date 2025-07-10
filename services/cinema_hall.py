from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall] | None:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> CinemaHall:
    new_or_existing_hall = (CinemaHall.objects
                            .get_or_create(name=hall_name,
                                           rows=hall_rows,
                                           seats_in_row=hall_seats_in_row)
                            )
    return new_or_existing_hall[0]
