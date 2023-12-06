from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> list:

    queryset = Movie.objects.all()
    if genres_ids is not None and actors_ids is not None:
        queryset = queryset.filter(
            genres__ids__in=genres_ids
        ).filter(
            actors__ids__in=actors_ids
        )
    if genres_ids is not None:
        queryset = queryset.filter(genres__ids__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__ids__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> str:
    return Movie.objects.all().filter(movie_id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:

    new_movie = Movie.objects.create(
        movie_title=movie_title,
        movie_description=movie_description
    )

    if genres_ids:
        new_movie.objects.set(genres_ids)

    if actors_ids:
        new_movie.objects.set(actors_ids)

    return new_movie
