from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__pk__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__pk__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
