# services/movie.py

from django.db.models import QuerySet
from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    """
    Retorna todos os filmes, opcionalmente filtrados por IDs de gêneros e/ou IDs de atores.

    :param genres_ids: Lista opcional de IDs de gêneros para filtrar os filmes.
    :param actors_ids: Lista opcional de IDs de atores para filtrar os filmes.
    :return: Um QuerySet de objetos Movie.
    """
    movies = Movie.objects.all()

    if genres_ids:
        # Filtra filmes que têm pelo menos um gênero dos IDs fornecidos
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        # Filtra filmes que têm pelo menos um ator dos IDs fornecidos
        movies = movies.filter(actors__id__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    """
    Retorna um filme pelo seu ID.

    :param movie_id: O ID do filme.
    :return: O objeto Movie correspondente ao ID.
    :raises Movie.DoesNotExist: Se nenhum filme com o ID fornecido for encontrado.
    """
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list = None,
    actors_ids: list = None
) -> Movie:
    """
    Cria um novo filme com o título e descrição fornecidos,
    opcionalmente adicionando gêneros e atores.

    :param movie_title: O título do filme.
    :param movie_description: A descrição do filme.
    :param genres_ids: Lista opcional de IDs de gêneros a serem associados ao filme.
    :param actors_ids: Lista opcional de IDs de atores a serem associados ao filme.
    :return: O objeto Movie recém-criado.
    """
    movie = Movie.objects.create(title=movie_title, description=movie_description)

    if genres_ids:
        # Adiciona gêneros ao filme. Certifica-se de que os gêneros existem.
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.add(*genres)
    if actors_ids:
        # Adiciona atores ao filme. Certifica-se de que os atores existem.
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.add(*actors)

    return movie

