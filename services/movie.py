from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = None, actors_ids: list = None) -> None:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        return movies.filter(genres__in=genres_ids, actors__in=actors_ids)
    elif genres_ids:
        return movies.filter(genres__in=genres_ids)
    elif actors_ids:
        return movies.filter(actors__in=actors_ids)
    else:
        return movies


def get_movie_by_id(movie_id: int) -> None:
    movie = Movie.objects.get(id=movie_id)

    if movie:
        return movie
    else:
        return None


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> None:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
