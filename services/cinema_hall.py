from db.models import CinemaHall


def get_cinema_halls() -> None:
    all_halls = CinemaHall.objects.all()
    return all_halls


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int
                       ) -> None:
    new_cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    return new_cinema_hall
