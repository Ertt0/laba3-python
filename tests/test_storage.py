import json

import pytest

from src.classrooms.catalog import Catalog
from src.classrooms.errors import CorruptedFile, InvalidEntity, UnsupportedFormatVersion
from src.classrooms.storage import load, save
from tests.constant import AUDIENCE1, AUDIENCE2


def test_round_trip_json(tmp_path):
    catalog1 = Catalog()
    catalog1.add(AUDIENCE1)
    catalog1.add(AUDIENCE2)

    file = tmp_path / "catalog1.json"
    save(catalog1, file)

    catalog2 = Catalog()
    load(catalog2, file)

    assert list(catalog2) == list(catalog1)


def test_corrupted_json():
    catalog1 = Catalog()
    catalog1.add(AUDIENCE1)

    with open("tests/broken.json", "w", encoding="utf-8") as f:
        f.write("ww")

    with pytest.raises(CorruptedFile):
        load(catalog1, "tests/broken.json")

    assert "Б-460" in catalog1


def test_change_after_error_load():
    catalog = Catalog()
    catalog.add(AUDIENCE1)
    bad_json = {
        "format_version": 1,
        "audiences": [
            AUDIENCE2.model_dump(mode="json"),
            {
                "id": "",
                "name": "плохая аудитория",
                "category": "lecture hall",
                "year": 2021,
                "specialization": "informatics",
                "building": "ГУК",
            },
        ],
    }

    with open("tests/change.json", "w", encoding="utf-8") as f:
        json.dump(bad_json, f)

    with pytest.raises(InvalidEntity):
        load(catalog, "tests/change.json")

    assert len(catalog) == 1
    assert "Б-460" in catalog
    assert "А-404" not in catalog


def test_unsupported_format(tmp_path):
    catalog = Catalog()
    bad_json = {
        "format_version": 2,
        "audiences": AUDIENCE2.model_dump(mode="json"),
    }

    file = tmp_path / "bad_version.json"

    with open(file, "w", encoding="utf-8") as f:
        json.dump(bad_json, f)

    with pytest.raises(UnsupportedFormatVersion):
        load(catalog, file)


def test_invalid_entinty(tmp_path):
    catalog = Catalog()
    bad_json = {
        "format_version": 1,
        "audiences": [
            {
                "id": "",
                "name": "плохая аудитория",
                "category": "lecture hall",
                "year": 2021,
                "specialization": "informatics",
                "building": "ГУК",
            }
        ],
    }

    file = tmp_path / "bad_entity.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(bad_json, f)

    with pytest.raises(InvalidEntity):
        load(catalog, file)
