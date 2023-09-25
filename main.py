import init_django_orm  # noqa: F401

from services.movie import get_movies


def main():
    yyy = get_movies()

    ttt = 0


if __name__ == "__main__":
    main()
