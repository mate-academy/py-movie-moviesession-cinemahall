from db.models import CinemaHall


def get_cinema_halls() -> CinemaHall.objects:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall.objects:
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )


def get_cinema_hall_by_id(hall_id: int) -> CinemaHall.objects:
    return CinemaHall.objects.get(id=hall_id)
