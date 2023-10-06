import re
from typing import Type


def all_ints(ls: list | None) -> bool:
    if ls is not None:
        values = [
            True if (isinstance(value, int) and value >= 1) else False
            for value in ls
        ]
        return all(values)
    return False


def is_date_correct(date: str | None) -> bool:
    if not isinstance(date, str):
        return False
    date_regex = re.compile(r"^(?:19|20\d\d)-"
                            r"(\d|0[1-9]|1[0-2])-"
                            r"(\d|0[1-9]|[1-2]\d|3[0-1])$"
                            )
    date_match = date_regex.search(date)
    return bool(date_match)


def is_table_item_exist(table: Type, item_id: int) -> bool:
    if item_id in [item.id for item in table.objects.all()]:
        return True
    return False
