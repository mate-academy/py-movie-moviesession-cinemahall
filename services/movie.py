from typing import Optional
from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: Optional[list[int]] = None,
               actors_ids: Optional[list[int]] = None
               ) -> QuerySet[Movie]:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    elif genres_ids and actors_ids:
        results = Movie.objects.filter(genres__id__in=genres_ids,
                                       actors__id__in=actors_ids).distinct()
        return results

    elif genres_ids and not actors_ids:
        results = Movie.objects.filter(genres__id__in=genres_ids)
        return results

    else:
        results = Movie.objects.filter(actors__id__in=actors_ids)
        return results



def get_movie_by_id(movie_id: int) -> Movie | None:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None
                 ) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)

    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
