from db.models import CinemaHall


def get_cinema_halls() -> str:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str, hall_rows: str,
                       hall_seats_in_row: str) -> str:
    new_cinema = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row)

    return new_cinema
