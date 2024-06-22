import init_django_orm  # noqa: F401

from db.models import Movie

from services.movie_session import update_movie_session


def main() -> None:
    Movie.objects.create(title="Madagascar", description="Madagascar movie")
    update_movie_session(session_id=3, movie_id=6)


if __name__ == "__main__":
    main()
