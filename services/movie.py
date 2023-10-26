from db.models import Genre, Actor, Movie
from django.db.models import QuerySet


def get_movies(genres_ids: list[Genre] = None,
               actors_ids: list[Actor] = None) -> QuerySet:
    queryset = Movie.objects.all()
    if actors_ids is None and genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if genres_ids is None and actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)
    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids,
                                   actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(id_of_movie: int) -> QuerySet:
    return Movie.objects.all().get(id=id_of_movie)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[Genre] = None,
                 actors_ids: list[Actor] = None) -> QuerySet:
    new_film = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if actors_ids:
        new_film.actors.set(actors_ids)
    if genres_ids:
        new_film.genres.set(genres_ids)
    return new_film


if __name__ == "__main__":
    get_movies()
