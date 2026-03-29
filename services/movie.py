from db.models import Movie


def get_movies(
    genres_ids: list[int] = None, actors_ids: list[int] = None
) -> list[Movie]:
    filters = {}
    if genres_ids:
        filters["genres__id__in"] = genres_ids
    if actors_ids:
        filters["actors__id__in"] = actors_ids
    return Movie.objects.filter(**filters)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
