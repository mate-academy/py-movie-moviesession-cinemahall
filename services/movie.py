from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return queryset
    if genres_ids and not actors_ids:
        return queryset.filter(genres__id__in=genres_ids)
    if actors_ids and not genres_ids:
        return queryset.filter(actors__id__in=actors_ids)
    if actors_ids and genres_ids:
        return queryset.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids
        )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
