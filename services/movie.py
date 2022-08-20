from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None):

    query_set = Movie.objects.all()

    if genres_ids is None and actors_ids is None:
        return query_set

    if genres_ids is not None and actors_ids is None:
        query_set = query_set.filter(genres__id__in=genres_ids)

    if genres_ids is None and actors_ids is not None:
        query_set = query_set.filter(actors__id__in=actors_ids)

    if genres_ids is not None and actors_ids is not None:
        query_set = query_set.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids)

    return query_set


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title,
        movie_description,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None):

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)

    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
