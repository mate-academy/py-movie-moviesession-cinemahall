import re
from typing import Type


def all_ints(ids_ls: list[int] | None) -> bool:
    if ids_ls is not None:
        values = [
            isinstance(value, int) and value >= 1
            for value in ids_ls
        ]
        return all(values)
    return False


def date_is_correct(date: str | None) -> bool:
    if not isinstance(date, str):
        return False
    date_regex = re.compile(r"^(?:19|20\d\d)-"
                            r"([1-9]|0[1-9]|1[0-2])-"
                            r"([1-9]|0[1-9]|[1-2]\d|3[0-1])$"
                            )
    date_match = date_regex.search(date)
    return bool(date_match)


def is_table_item_exist(table: Type, item_id: int) -> bool:
    return table.objects.filter(id=item_id).exists()


def ids_are_corrects_and_exist(ids: list | None, table: Type) -> bool:
    return all_ints(ids) and all(is_table_item_exist(table, id_)
                             for id_ in ids)

