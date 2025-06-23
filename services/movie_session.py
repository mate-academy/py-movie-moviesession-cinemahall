# services/movie_session.py

import datetime
from django.db.models import QuerySet
from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
    movie_show_time: datetime.datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    """
    Cria uma nova sessão de filme.

    :param movie_show_time: A data e hora da sessão do filme.
    :param movie_id: O ID do filme a ser exibido.
    :param cinema_hall_id: O ID da sala de cinema onde a sessão ocorrerá.
    :return: O objeto MovieSession recém-criado.
    :raises Movie.DoesNotExist: Se o filme com o ID fornecido não for
                                encontrado.
    :raises CinemaHall.DoesNotExist: Se a sala de cinema com o ID fornecido
                                     não for encontrada.
    """
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie=movie,
        cinema_hall=cinema_hall
    )
    return movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    """
    Retorna todas as sessões de filmes, opcionalmente filtradas por data.

    :param session_date: Uma string opcional no formato "YYYY-MM-DD" para
                         filtrar as sessões por data.
    :return: Um QuerySet de objetos MovieSession.
    """
    movie_sessions = MovieSession.objects.all()

    if session_date:
        # Filtra sessões pela data. O sufixo __date permite comparar apenas
        # a data de um DateTimeField.
        movie_sessions = movie_sessions.filter(show_time__date=session_date)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    """
    Retorna uma sessão de filme pelo seu ID.

    :param movie_session_id: O ID da sessão do filme.
    :return: O objeto MovieSession correspondente ao ID.
    :raises MovieSession.DoesNotExist: Se nenhuma sessão com o ID fornecido
                                       for encontrada.
    """
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime.datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None
) -> MovieSession:
    """
    Atualiza uma sessão de filme existente.

    :param session_id: O ID da sessão do filme a ser atualizada.
    :param show_time: Novo horário de exibição opcional.
    :param movie_id: Novo ID de filme opcional.
    :param cinema_hall_id: Novo ID de sala de cinema opcional.
    :return: O objeto MovieSession atualizado.
    :raises MovieSession.DoesNotExist: Se nenhuma sessão com o ID fornecido
                                       for encontrada.
    :raises Movie.DoesNotExist: Se o novo filme com o ID fornecido não for
                                encontrado.
    :raises CinemaHall.DoesNotExist: Se a nova sala de cinema com o ID
                                     fornecido não for encontrada.
    """
    movie_session = Movie.objects.get(id=session_id)

    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie = Movie.objects.get(id=movie_id)
    if cinema_hall_id is not None:
        movie_session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    """
    Exclui uma sessão de filme pelo seu ID.

    :param session_id: O ID da sessão do filme a ser excluída.
    :raises MovieSession.DoesNotExist: Se nenhuma sessão com o ID fornecido
                                       for encontrada.
    """
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
