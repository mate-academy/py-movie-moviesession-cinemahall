from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession


class MovieSessionService:
    @staticmethod
    def create_movie_session(
            movie_show_time: datetime,
            movie_id: int,
            cinema_hall_id: int
    ) -> None:
        MovieSession.objects.create(
            show_time=movie_show_time,
            cinema_hall_id=cinema_hall_id,
            movie_id=movie_id
        )

    @staticmethod
    def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
    ) -> None:
        updated_session = MovieSessionService.get_movie_session_by_id(
            session_id
        )
        if show_time:
            updated_session.show_time = show_time
        if movie_id:
            updated_session.movie_id = movie_id
        if cinema_hall_id:
            updated_session.cinema_hall_id = cinema_hall_id
        updated_session.save()

    @staticmethod
    def get_movies_sessions(
        session_date: str | None = None
    ) -> QuerySet[MovieSession]:
        queryset = MovieSession.objects.all()
        if session_date:
            queryset = queryset.filter(show_time__date=session_date)
        return queryset

    @staticmethod
    def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
        return MovieSession.objects.get(pk=movie_session_id)

    @staticmethod
    def delete_movie_session_by_id(movie_session_id: int) -> None:
        session_to_delete = MovieSessionService.get_movie_session_by_id(
            movie_session_id
        )
        session_to_delete.delete()
