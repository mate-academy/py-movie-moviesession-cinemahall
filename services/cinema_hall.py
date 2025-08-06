from django.db.models import QuerySet
from django.core.exceptions import ObjectDoesNotExist

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def get_cinema_halls_by_id(hall_id: int) -> CinemaHall | None:
    try:
        return CinemaHall.objects.get(id=hall_id)
    except ObjectDoesNotExist as e:
        print(e)
    except ValueError as e:
        print(e)
    return None


def create_cinema_hall(
        hall_name: str,
        hall_rows: int,
        hall_seats_in_row: int
) -> CinemaHall:
    obj, created = CinemaHall.objects.get_or_create(
        name=hall_name,
        defaults={
            "rows": hall_rows,
            "seats_in_row": hall_seats_in_row
        }
    )
    return obj
