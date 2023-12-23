from django.db.models import QuerySet


from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def get_cinema_hall_by_id(hall_id: int) -> QuerySet[CinemaHall]:
    return CinemaHall.objects.filter(id=hall_id)


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> None:

    CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row)
