from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None):
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int = None):
    queryset = Movie.objects.all()
    if movie_id is not None:
        queryset.filter(id=movie_id)
    return queryset


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
):
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        movie.actors.set(actors_ids)
    if actors_ids is not None:
        movie.genres.set(genres_ids)

    return movie
