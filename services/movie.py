from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None):
    take_movie = Movie.objects.all()
    if genres_ids:
        take_movie = take_movie.filter(genres__id__in=genres_ids)
    if actors_ids:
        take_movie = take_movie.filter(actors__id__in=actors_ids)
    return take_movie


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None):

    add_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        add_movie.genres.set(genres_ids)
    if actors_ids:
        add_movie.actors.set(actors_ids)
    return add_movie
