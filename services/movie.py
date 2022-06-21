from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None):
    movie_queryset = Movie.objects.all()
    if genres_ids:
        movie_queryset = movie_queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie_queryset = movie_queryset.filter(actors__id__in=actors_ids)
    return movie_queryset


def get_movie_by_id(movie_id: int):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None):
    movie_queryset = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie_queryset.genres.set(genres_ids)
    if actors_ids:
        movie_queryset.actors.set(actors_ids)
    return movie_queryset
