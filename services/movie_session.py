from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession

def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int
                         ) -> MovieSession:
    pass
