from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Category(Enum):
    LECTURE_HALL = "lecture hall"
    SEMINAR_ROOM = "seminar room"
    LABORATORY = "laboratory"
    ASSEMBLY_HALL = "assembly hall"


class Specialization(Enum):
    PHYSICS = "physics"
    MATHEMATICS = "mathematics"
    INFORMATICS = "informatics"
    HISTORY = "history"
    CHEMISTRY = "chemistry"
    PHILOSOPHY = "philosophy"


class Audience(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    category: Category
    year: int = Field(gt=1969, lt=2027)
    specialization: Specialization
    building: str = Field(min_length=1)
