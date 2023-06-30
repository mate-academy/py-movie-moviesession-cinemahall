import init_django_orm  # noqa: F401
from services.movie_session import get_movies_sessions


if __name__ == "__main__":
    sessions_1 = get_movies_sessions("2019-8-19")
    print(sessions_1)
