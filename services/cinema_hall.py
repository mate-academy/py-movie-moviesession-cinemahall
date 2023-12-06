from db.models import CinemaHall


def get_cinema_halls() -> list:
    return CinemaHall.object.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    new_cinema_hall = CinemaHall.objects.create(
        hall_name=hall_name,
        hall_rows=hall_rows,
        hall_seats_in_row=hall_seats_in_row
    )

    return new_cinema_hall
