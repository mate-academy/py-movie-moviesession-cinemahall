import init_django_orm  # noqa: F401
from typing import List, Optional
from db.models import Genre, Actor, Movie


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> list:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            genre__id__in=genres_ids,
            actor__id__in=actors_ids
        ).distinct()
    elif genres_ids:
            movies = movies.filter(genre__id__in=genres_ids).distinct()
    elif actors_ids:
            movies = movies.filter(actor__id__in=actors_ids).distinct()

    return list(movies)

def get_movie_by_id(movie_id: int) -> Optional[Movie]:
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[list[int]] = None,
                 actors_ids: Optional[list[int]] = None
                 ) -> Optional[Movie]:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
