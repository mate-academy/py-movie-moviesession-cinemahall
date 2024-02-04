from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> any:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        movies_with_one_genre_and_actors = Movie.objects.filter(
            genres__in=genres_ids, actors__in=actors_ids
        )
        return movies_with_one_genre_and_actors

    if genres_ids:
        query_set_with_genres = Movie.objects.filter(genres__in=genres_ids)
        return query_set_with_genres

    if actors_ids:
        query_set_with_actors = Movie.objects.filter(actors__in=actors_ids)
        return query_set_with_actors


def get_movie_by_id(movie_id: int) -> any:
    return Movie.objects.get(pk=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
