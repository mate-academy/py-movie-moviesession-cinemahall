from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        actors_ids: list[int] = None,
        genres_ids: list[int] = None,
) -> QuerySet[Movie]:

    queryset = Movie.objects.filter()

    if not actors_ids and not genres_ids:
        return queryset

    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if actors_ids:
        movie.actors.add(*actors_ids)

    if genres_ids:
        movie.genres.add(*genres_ids)

    return movie
