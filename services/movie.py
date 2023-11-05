from db.models import Movie


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:

    films = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()

    if genres_ids is not None and actors_ids is not None:
        films = (
            Movie.objects.filter(genres__id__in=genres_ids).
            filter(actors__id__in=actors_ids)
        )

    if actors_ids is None:
        films = (
            Movie.objects.
            filter(genres__id__in=genres_ids)
        )

    if genres_ids is None:
        films = Movie.objects.filter(actors__id__in=actors_ids)

    return films


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:

    film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        film.genres.set(genres_ids)
    if actors_ids:
        film.actors.set(actors_ids)

    return film
