from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> str:
    query = Movie.objects.all()
    if genres_ids:
        query = query.filter(genres__id__in=genres_ids)
    if actors_ids:
        query = query.filter(actors__id__in=actors_ids)
    return query.distinct()


def get_movie_by_id(movie_id: int) -> str:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list = None,
    actors_ids: list = None
) -> str:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
