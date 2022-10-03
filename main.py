import init_django_orm  # noqa: F401

from db.models import Genre, Actor, Movie, CinemaHall, MovieSession

import json

from services import movie, cinema_hall, movie_session


def main():
    with open("cinema_db_data.json", "r") as file_json:
        data_json = json.load(file_json)
    for data in data_json:
        if data["model"] == "db.cinemahall":
            if not CinemaHall.objects.filter(pk=data["pk"]).exists():
                CinemaHall.objects.create(
                    pk=data["pk"],
                    name=data["fields"]["name"],
                    rows=data["fields"]["rows"],
                    seats_in_row=data["fields"]["seats_in_row"]
                )
        elif data["model"] == "db.genre":
            if not Genre.objects.filter(pk=data["pk"]).exists():
                Genre.objects.create(
                    pk=data["pk"],
                    name=data["fields"]["name"]
                )
        elif data["model"] == "db.actor":
            if not Actor.objects.filter(pk=data["pk"]).exists():
                Actor.objects.create(
                    pk=data["pk"],
                    first_name=data["fields"]["first_name"],
                    last_name=data["fields"]["last_name"]
                )
        elif data["model"] == "db.movie":
            if not Movie.objects.filter(pk=data["pk"]).exists():
                movie_ = Movie.objects.create(
                    pk=data["pk"],
                    title=data["fields"]["title"],
                    description=data["fields"]["description"]
                )
                movie_.genres.set(data["fields"]["genres"])
                movie_.actors.set(data["fields"]["actors"])
        elif data["model"] == "db.moviesession":
            if not MovieSession.objects.filter(pk=data["pk"]).exists():
                MovieSession.objects.create(
                    pk=data["pk"],
                    show_time=data["fields"]["show_time"],
                    movie=Movie.objects.get(pk=data["fields"]["movie"]),
                    cinema_hall=CinemaHall.objects.get(
                        pk=data["fields"]["cinema_hall"])
                )


if __name__ == "__main__":
    main()
    # print(movie.get_movies(actors_ids=[1, 2]))
    # print(movie.get_movie_by_id(movie_id=2))
    # print(movie.create_movie(
    #     movie_title="New_movie",
    #     movie_description="New_description",
    #     genres_ids=[1],
    #     actors_ids=[2, 4]
    # ))
    # print(CinemaHall.objects.get(id=1).capacity())
    # print(cinema_hall.get_cinema_halls())
    # print(cinema_hall.create_cinema_hall(
    #     hall_name="My Hall",
    #     hall_rows=16,
    #     hall_seats_in_row=24
    # ))
    # print(movie_session.get_movie_session_by_id(movie_session_id=1))
    print(movie_session.get_movies_sessions(session_date="2024-10-09"))
    # print(movie_session.get_movies_sessions())
    # print(movie_session.create_movie_session(
    # datetime.datetime(2023, 11, 2, 20, 30), 1, 2))
    # print(movie_session.update_movie_session(
    # 7, datetime.datetime(2023, 11, 2, 19, 20), 1, 2))
    # print(movie_session.delete_movie_session_by_id(session_id=6))
    # print()
