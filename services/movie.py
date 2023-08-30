from db.models import Movie


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> list[Movie]:
    queryset = Movie.objects.all()
    if None not in (genres_ids, actors_ids):
        return queryset.filter(
            actors__id__in=actors_ids,
            genres__id__in=genres_ids,
        )
    elif actors_ids is None and genres_ids is not None:
        return queryset.filter(genres__id__in=genres_ids)
    elif actors_ids is not None and genres_ids is None:
        return queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)
    return new_movie
