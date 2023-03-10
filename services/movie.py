from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None) -> list[Movie]:
    all_movies = Movie.objects.all()

    if genres_ids:
        all_movies = Movie.objects.filter(genres__in=genres_ids)

    if actors_ids:
        all_movies = Movie.objects.filter(actors__in=genres_ids)

    return all_movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_id: list[int] = None,
        actors_id: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_id:
        movie.genres.set(genres_id)

    if actors_id:
        movie.actors.set(actors_id)

    return movie
