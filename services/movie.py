from django.db.models import QuerySet

from db.models import Movie


def get_movies(**kwargs) -> QuerySet:
    genres_ids = kwargs.get("genres_ids")
    actors_ids = kwargs.get("actors_ids")
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(id_: int) -> Movie | None:
    return Movie.objects.filter(id=id_).get()


def create_movie(movie_title: str, movie_description: str, **kwargs) -> None:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if kwargs.get("genres_ids"):
        movie.genres.add(*kwargs.get("genres_ids"))
    if kwargs.get("actors_ids"):
        movie.actors.add(*kwargs.get("actors_ids"))
