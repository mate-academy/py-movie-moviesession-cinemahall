from db.models import Movie


def get_movies(
        genres_ids: list[int],
        actors_ids: list[int] = None
) -> list[Movie]:
    movies = Movie.objects.filter(__id__in=genres_ids)
    if actors_ids is not None:
        movies = movies.filter(id__in=actors_ids)
    return list(movies)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.filter(id=movie_id).get()


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    return Movie.objects.create(
        title=movie_title,
        description=movie_description,
        genres=genres_ids,
        actors=actors_ids
    )
