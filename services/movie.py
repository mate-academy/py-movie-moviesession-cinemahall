from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: int = None,
        actors_ids: int = None
) -> QuerySet | Movie:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = Movie.objects.filter(
            genres__in=genres_ids,
            actors__in=actors_ids)
    elif genres_ids:
        queryset = Movie.objects.filter(genres__in=genres_ids)
    elif actors_ids:
        queryset = Movie.objects.filter(actors__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.add(*genres_ids)

    if actors_ids:
        movie.actors.add(*actors_ids)
    return movie
