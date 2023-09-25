from typing import List

from db.models import Genre, Actor, Movie


def get_movies(genders_ids: List[Genre] = None, actors_ids: List[Actor] = None) -> List[Movie]:
    uuu = 0
    queryset = Movie.objects.all()

    if genders_ids is None and actors_ids is None:
        return queryset
    if genders_ids is not None and actors_ids is not None:
        queryset = queryset.filter(genders__id__in=genders_ids, actors__id_in=actors_ids)
        return queryset
    if genders_ids is not None and actors_ids is None:
        queryset = queryset.filter(genders__id__in=genders_ids)
        return queryset
    if actors_ids is not None and genders_ids is None:
        queryset = queryset.filter( actors__id_in=actors_ids)
        return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(__id=movie_id)


def create_movie(movie_title: str, movie_description: str, genres_ids: List[Genre] = None,
                 actors_ids: List[Actor] = None) -> None:
    new_movie = Movie.objects.create(title=movie_title, description=movie_description,)
    if genres_ids:
        new_movie.genres.set(genres_ids)
    if actors_ids:
        new_movie.actors.set(actors_ids)

    return new_movie
