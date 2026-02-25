from db.models import Movie, Genre, Actor


def get_movies(
    genres_ids: list = None,
    actors_ids: list = None
) -> list[Movie]:

    queryset = Movie.objects.all()

    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list = None,
    actors_ids: list = None
) -> None:

    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if genres_ids is not None:
        genres = Genre.objects.filter(id__in=genres_ids)
        for gen in genres:
            movie.genres.add(gen)

    if actors_ids is not None:
        actors = Actor.objects.filter(id__in=actors_ids)
        for act in actors:
            movie.actors.add(act)
