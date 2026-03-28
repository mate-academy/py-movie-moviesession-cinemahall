from db.models import CinemaHall


def get_cinema_halls(cinema_hall_name: str = None) -> CinemaHall:
    queryset = CinemaHall.objects.all()
    if cinema_hall_name:
        queryset.filter(name__id__in=cinema_hall_name)

    return queryset


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int
                       ) -> CinemaHall:
    create_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row)

    return create_hall
