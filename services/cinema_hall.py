from db.models import CinemaHall


def get_cinema_hall() -> CinemaHall:
    query_set = CinemaHall.objects.all()
    return query_set

def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row
) -> None:
    CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )