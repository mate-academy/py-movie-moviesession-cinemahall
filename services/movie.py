from db.models import Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None) -> list[QuerySet[Movie, Movie]]:

    if genres_ids and actors_ids:
        return Movie.objects.filter(id__in=genres_ids).filter(id__in=actors_ids)

    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres_id__in=genres_ids)

    if actors_ids:
        queryset = queryset.filter(actors_id__in=actors_ids)

    return queryset

def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)

def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> Movie:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.genres.set(actors_ids)

    return new_movie

