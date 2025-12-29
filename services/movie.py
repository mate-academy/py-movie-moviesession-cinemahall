from typing import List, Optional
from django.db.models import Q
from db.models import Movie, Genre, Actor


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None) -> List[Movie]:
    filters = Q()

    if genres_ids:
        filters &= Q(genres__id__in=genres_ids)

    if actors_ids:
        filters &= Q(actors__id__in=actors_ids)

    return Movie.objects.filter(filters).distinct()


def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    try:
        return Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return None


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
