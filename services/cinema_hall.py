from db.models import CinemaHall


def get_cinema_halls() -> CinemaHall:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:
    _, _ = CinemaHall.objects.get_or_create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
