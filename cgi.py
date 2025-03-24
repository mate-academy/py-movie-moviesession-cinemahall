class FieldStorage:
    def __init__(self, *args, **kwargs) -> None:
        self.list = []

    def __iter__(self) -> "FieldStorage":
        return self
