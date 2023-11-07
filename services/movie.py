from typing import Optional

from django.db.models import Q

from db.models import Movie, Genre, Actor


def get_movies(genres_ids: Optional[list] = None, actors_ids: Optional[list] = None):
    if not genres_ids and not actors_ids:
        return Movie.objects.all()
    elif genres_ids and actors_ids:
        return Movie.objects.filter(Q(genres__in=genres_ids) & Q(actors__in=actors_ids))
    elif genres_ids and not actors_ids:
        return Movie.objects.filter(genres__in=genres_ids)
    elif not genres_ids and actors_ids:
        return Movie.objects.filter(actors__in=actors_ids)


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(pk=movie_id)


def create_movie(movie_title: str, movie_description: str, genres_ids: Optional[list] = None,
                 actors_ids: Optional[list] = None):
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )

    if genres_ids:
        movie.genres.add(*Genre.objects.filter(id__in=genres_ids))

    if actors_ids:
        movie.actors.add(*Actor.objects.filter(id__in=actors_ids))

    movie.save()