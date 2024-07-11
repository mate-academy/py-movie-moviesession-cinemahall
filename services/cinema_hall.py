from db.models import CinemaHall


def get_cinema_halls() -> CinemaHall:
    all_cinema = CinemaHall.objects.all()
    return all_cinema


def create_cinema_hall(
        hall_name: str, hall_rows: int, hall_seats_in_row: int
) -> CinemaHall:
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
