import pytest

from src.classrooms.catalog import Catalog
from src.classrooms.errors import DuplicateID
from src.classrooms.models import Category
from tests.constant import AUDIENCE1, AUDIENCE2


def test_add():
    catalog = Catalog()
    catalog.add(AUDIENCE1)

    assert "Б-460" in catalog


def test_get():
    catalog = Catalog()
    catalog.add(AUDIENCE1)
    res = catalog.get("Б-460")

    assert res == AUDIENCE1


def test_remove():
    catalog = Catalog()
    catalog.add(AUDIENCE1)
    catalog.remove("Б-460")

    assert "Б-460" not in catalog


def test_duplicate_id():
    catalog = Catalog()
    catalog.add(AUDIENCE1)

    with pytest.raises(DuplicateID):
        catalog.add(AUDIENCE1)


def test_find_by_category():
    catalog = Catalog()
    catalog.add(AUDIENCE1)
    res = catalog.find_by_category(Category.LECTURE_HALL)

    assert res == [AUDIENCE1]


def test_find_by_name():
    catalog = Catalog()
    catalog.add(AUDIENCE1)
    res = catalog.find_by_name("АУДИТОРия 460")

    assert res == [AUDIENCE1]


def test_iter():
    catalog = Catalog()
    catalog.add(AUDIENCE1)
    catalog.add(AUDIENCE2)
    res = [audience.id for audience in catalog]

    assert res == ["А-404", "Б-460"]
