import pytest
from pydantic import ValidationError

from src.classrooms.models import Audience, Category, Specialization
from tests.constant import AUDIENCE1


def test_valid_audience():
    audience = AUDIENCE1

    assert audience.building == "ГУК"


def test_invalid_audience():
    with pytest.raises(ValidationError):
        Audience(
            id="А-404",
            name="Ну такой нормальный кабинет",
            category=Category.SEMINAR_ROOM,
            year=2077,
            specialization=Specialization.PHILOSOPHY,
            building="3",
        )
