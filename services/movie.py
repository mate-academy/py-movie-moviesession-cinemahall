from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> list[Movie]:
    movies = Movie.objects.all()
    if genres_ids is None and actors_ids is None:
        return movies
    if genres_ids and actors_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )
        return movies.distinct()
    if genres_ids:
        movies = Movie.objects.filter(genres__id__in=genres_ids)
        return movies.distinct()
    if actors_ids:
        movies = Movie.objects.filter(actors__id__in=actors_ids)
        return movies.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    movie = Movie.objects.get(id=movie_id)
    return movie


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)

    if actors_ids:
        movie.actors.set(actors_ids)

    return movie
