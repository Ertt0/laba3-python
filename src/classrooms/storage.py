import json

from pydantic import ValidationError

from src.classrooms.errors import (
    CorruptedFile,
    DuplicateID,
    InvalidEntity,
    UnsupportedFormatVersion,
)
from src.classrooms.models import Audience


def save(catalog, file):
    audiences = [i.model_dump(mode="json") for i in catalog.items.values()]
    data = {
        "format_version": 1,
        "audiences": audiences,
    }
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load(catalog, file):
    with open(file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise CorruptedFile("Поврежденный JSON-файл")

    if data["format_version"] != 1:
        raise UnsupportedFormatVersion("Неверный формат версии")

    cur_items = {}
    for item in data["audiences"]:
        try:
            audience = Audience(**item)
        except ValidationError:
            raise InvalidEntity("Некорректные данные аудитории")
        if audience.id in cur_items:
            raise DuplicateID("ID уже есть в каталоге")
        else:
            cur_items[audience.id] = audience

    catalog.items = cur_items
