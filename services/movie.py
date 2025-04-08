from db.models import Movie

from django.db.models import QuerySet


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> QuerySet | Movie:
    queryset = Movie.objects.all()
    if genres_ids is None and actors_ids is None:
        return queryset

    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)
        return queryset

    if not actors_ids and genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
        return queryset

    if not genres_ids and actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
        return queryset


def get_movie_by_id(id_: int = None) -> QuerySet | Movie:
    return Movie.objects.get(id=id_)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie


