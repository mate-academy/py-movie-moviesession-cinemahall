from db.models import Movie


def get_movies(
        genres_ids: int = None,
        actors_ids: list[int] = None
) -> list[Movie]:

    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres_id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors_id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None
) -> None:

    new_movie = Movie.objects.create(
        movie_title=movie_title,
        movie_description=movie_description
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)
