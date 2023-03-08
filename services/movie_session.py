

from db.models import *


def create_movie_session(movie_show_time, movie_id, cinema_hall_id):
    return MovieSession.objects.create(
        show_time=movie_show_time, movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id))


def get_movies_sessions(session_date=None):
    queryset = MovieSession.objects.all()
    if session_date is not None:
        # print(session_date.split("-")[0])
        # print(session_date.split("-")[1])
        # print(session_date.split("-")[2])
        queryset = queryset.filter(show_time__year=session_date.split("-")[0],
                                   show_time__month=session_date.split("-")[1],
                                   show_time__day=session_date.split("-")[2])
    return queryset


def get_movie_session_by_id(movie_session_id):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id, show_time=None, movie_id=None, cinema_hall_id=None):
    ms = MovieSession.objects.filter(id=session_id)

    if show_time:
        ms.update(show_time=show_time)
    if movie_id:
        ms.update(movie=movie_id)
    if cinema_hall_id:
        ms.update(cinema_hall=cinema_hall_id)

    return ms


def delete_movie_session_by_id(session_id):
    return MovieSession.objects.filter(id=session_id).delete()

