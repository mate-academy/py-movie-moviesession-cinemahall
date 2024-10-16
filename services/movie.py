from django.db.models import QuerySet

from db.models import Actor, Genre, Movie


def get_movies(genres_ids: list[Genre] = None,
               actors_ids: list[Actor] = None
               ) -> QuerySet:
    queryset = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return queryset
    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__in=genres_ids, actors__in=actors_ids)
        return queryset
    if genres_ids and not actors_ids:
        queryset = queryset.filter(genres__in=genres_ids)
        return queryset
    if not genres_ids and actors_ids:
        queryset = queryset.filter(actors__in=actors_ids)
        return queryset


def get_movie_by_id(id_: int) -> Movie:
    return Movie.objects.get(id=id_)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None
                 ) -> None:
    film = Movie.objects.create(title=movie_title, description=movie_description)
    if genres_ids:
        film.genres.add(*genres_ids)
        film.save()
    if actors_ids:
        film.actors.add(*actors_ids)
        film.save()
