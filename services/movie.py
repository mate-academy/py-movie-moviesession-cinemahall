from db.models import Movie


def get_movie_by_id(movie_id: int) -> None:
    return Movie.objects.get(id=movie_id)


def get_movies(genres_ids: int = None, actors_ids: int = None) -> None:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies.distinct()


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: int = None,
                 actors_ids: int = None) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)

    if genres_ids:
        movie.genres.add(*genres_ids)

    if actors_ids:
        movie.actors.add(*actors_ids)

    return movie
