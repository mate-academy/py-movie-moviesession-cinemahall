from db.models import Actor


def get_actors() -> list[Actor]:
    return Actor.objects.all()


def create_actor(first_name: str, last_name: str) -> Actor:
    return Actor.objects.create(first_name=first_name, last_name=last_name)
