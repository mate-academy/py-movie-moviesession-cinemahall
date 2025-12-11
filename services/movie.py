# services/movie.py

from typing import Optional, List
from django.db.models import QuerySet
# Importujemy wszystkie potrzebne modele
from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None
) -> QuerySet[Movie]:
    """
    Pobiera filmy, opcjonalnie filtrując po identyfikatorach gatunków i aktorów.
    """
    queryset = Movie.objects.all()

    if genres_ids:
        # Filtr dla gatunków: filmy, które mają co najmniej jeden gatunek z listy
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids:
        # Filtr dla aktorów: filmy, które mają co najmniej jednego aktora z listy
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    """
    Pobiera film o podanym ID.
    """
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: Optional[List[int]] = None,
        actors_ids: Optional[List[int]] = None,
) -> Movie:
    """
    Tworzy nowy film i przypisuje mu opcjonalne gatunki i aktorów.
    """
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    # Przypisanie gatunków
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)

    # Przypisanie aktorów
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)

    return movie
