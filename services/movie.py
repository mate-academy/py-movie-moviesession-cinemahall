from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> Movie:
    all_movie = Movie.objects.all()
    if genres_ids is None and actors_ids is None:
        return all_movie
    if genres_ids and actors_ids is None:
        return all_movie.filter(genres__id__in=genres_ids)
    if actors_ids and genres_ids is None:
        return all_movie.filter(actors__id__in=actors_ids)
    if genres_ids and actors_ids:
        return all_movie.filter(genres__id__in=genres_ids).filter(
            actors__id__in=actors_ids
        )


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None) -> None:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
