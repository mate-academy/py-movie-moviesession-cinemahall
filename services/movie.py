from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> list[Movie]:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(
            genres_id__in=genres_ids,
            actors_id__in=actors_ids
        )

    if genres_ids:
        return Movie.objects.filter(genres_id__in=genres_ids)

    if actors_ids:
        return Movie.objects.filter(actors_id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    new_movie = Movie(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        new_movie.genres.add(*genres_ids)

    if actors_ids:
        new_movie.actors.add(*actors_ids)

    return new_movie
