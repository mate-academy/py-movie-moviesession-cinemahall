from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:

    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> None:
    return Movie.objects.filter(id=movie_id).get()


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if actors_ids:
        movie.actors.set(actors_ids)
    if genres_ids:
        movie.genres.set(genres_ids)

    return movie
