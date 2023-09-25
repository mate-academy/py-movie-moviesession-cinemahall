from typing import List

from db.models import Genre, Actor, Movie


def get_movies(genders_ids: List[Genre] = None, actors_ids: List[Actor] = None) -> List[Movie]:
    uuu = 0
    list_movies = []
    if not genders_ids and not actors_ids:
        for movie in Movie.objects.all():
#            print(movie)
            list_movies.append(movie)

    if genders_ids and actors_ids:
        pass

    return list_movies


def get_movie_by_id(movie_id: int) -> Movie:
    pass


def create_movie(movie_title: str, movie_description: str, genres_ids: List[Genre] = None,
                 actors_ids: List[Actor] = None) -> None:
    pass

