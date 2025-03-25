from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


