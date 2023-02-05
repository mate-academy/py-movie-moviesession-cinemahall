from db.models import CinemaHall


def get_cinema_halls() -> list[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:

    CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )


def get_cinema_halls_by_id(cinema_hall_id: int) -> CinemaHall:
    return CinemaHall.objects.get(id=cinema_hall_id)
