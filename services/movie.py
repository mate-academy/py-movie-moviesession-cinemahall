from db.models import Movie


def get_movies(
        genres_ids: str = None,
        actors_ids: str = None
) -> list:
    if genres_ids is None and actors_ids is None:
        return Movie.objects.all()
    elif genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids,
        ).distinct()
    elif genres_ids is not None:
        return Movie.objects.filter(
            genres__id__in=genres_ids).distinct()
    elif actors_ids is not None:
        return Movie.objects.filter(
            actors__id__in=actors_ids).distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: str = None,
        actors_ids: str = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        movie.genres.add(*genres_ids)

    if actors_ids is not None:
        movie.actors.add(*actors_ids)

    return movie
