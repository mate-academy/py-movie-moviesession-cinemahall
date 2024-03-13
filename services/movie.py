from db.models import Genre, Movie, MovieSession, Actor, CinemaHall
import init_django_orm


def get_movie(genres_ids=None, actor_ids=None):
    if genres_ids is None and actor_ids is None:
        return Movie.objects.all()
