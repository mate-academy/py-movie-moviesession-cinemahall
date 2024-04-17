from django.db.models import QuerySet


from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    created_cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats=hall_seats_in_row
    )
    return created_cinema_hall
