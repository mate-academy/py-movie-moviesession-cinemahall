from django.db.models import QuerySet


from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    queryset = Movie.objects.all()

    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids).distinct()

    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None,
                 ) -> Movie:
    new_film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_film.genres.set(genres_ids)

    if actors_ids:
        new_film.actors.set(actors_ids)

    return new_film
