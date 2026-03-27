import init_django_orm  # noqa: F401

from db.models import Genre, Actor, Movie, CinemaHall, MovieSession

import json

from services import movie, cinema_hall, movie_session


def main() -> None:
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
