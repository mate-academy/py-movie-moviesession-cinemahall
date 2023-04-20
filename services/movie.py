from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> Movie:
    got_movies = Movie.objects.all()
    if genres_ids:
        got_movies = got_movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        got_movies = got_movies.filter(actors__id__in=actors_ids)
    return got_movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


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
