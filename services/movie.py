from typing import List, Optional

from django.db.models import QuerySet, Q

from db.models import Movie, Actor, Genre


def get_movie(genres_ids: List[Genre] = None,
              actors_ids: List[Actor] = None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids and actors_ids:
        return queryset.filter(Q(genres__id__in=genres_ids)
                               & Q(actors__id__in=actors_ids)).distinct()
    elif genres_ids:
        return queryset.filter(genre_id__in=genres_ids)
    elif actors_ids:
        return queryset.filter(actor_id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: Optional[List[int]] = None,
    actors_ids: Optional[List[int]] = None
) -> Movie:

    new_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        new_movie.genres.add(*genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        new_movie.actors.add(*actors)

    return new_movie
