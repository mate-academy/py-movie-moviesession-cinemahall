from db.models import Movie


def get_movies(
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> list[Movie]:
    filters = {}
    if genres_ids:
        filters["genres__id__in"] = genres_ids
    if actors_ids:
        filters["actors__id__in"] = actors_ids

    return Movie.objects.filter(**filters)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] | None = None,
        actors_ids: list[int] | None = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        for genre_id in genres_ids:
            new_movie.genres.add(genre_id)

    if actors_ids:
        for actor_id in actors_ids:
            new_movie.actors.add(actor_id)

    return new_movie
