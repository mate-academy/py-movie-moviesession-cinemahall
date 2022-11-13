from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> list:
    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie.objects:
    if movie_id is not None:
        return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> Movie.objects:
    new_movie = Movie.objects.create(title=movie_title,
                                     description=movie_description
                                     )
    if genres_ids:
        new_movie.objects.set(genres_ids)

    if actors_ids:
        new_movie.objects.set(actors_ids)

    return new_movie
