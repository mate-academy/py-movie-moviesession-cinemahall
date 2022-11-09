from db.models import Movie, Genre, Actor


def get_movies(genres_ids: int = None, actors_ids: int = None) -> str:
    filter_args = {}
    if genres_ids is not None:
        filter_args["genres__id__in"] = genres_ids
    if actors_ids is not None:
        filter_args["actors__id__in"] = actors_ids
    movies = Movie.objects.filter(**filter_args)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.filter(id=movie_id).first()


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list[int] = None,
        genres_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        genres = Genre.objects.filter(pk__in=genres_ids)
        movie.genres.set(genres)
    if actors_ids:
        actors = Actor.objects.filter(pk__in=actors_ids)
        movie.actors.set(actors)
    return movie
