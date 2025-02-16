from db.models import CinemaHall


def get_cinema_halls() -> list:
    return CinemaHall.objects.all()


def create_cinema_hall(
    hall_name: str,
    rows: int,
    hall_rows: int
) -> None:
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=rows,
        seats_in_row=hall_rows
    )
    return cinema_hall
