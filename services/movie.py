from db.models import Movie


def get_movies(genres_ids: list[int] = None, actors_ids: list[int] = None) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        )

    if not genres_ids and actors_ids:
        movies = Movie.objects.filter(
            actors__id__in=actors_ids
        )

    if genres_ids and not actors_ids:
        movies = Movie.objects.filter(
            genres__id__in=genres_ids,
        )

    if not genres_ids and not actors_ids:
        return movies
