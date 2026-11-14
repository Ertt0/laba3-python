from src.classrooms.models import Audience, Category, Specialization

AUDIENCE1 = Audience(
    id="Б-460",
    name="Аудитория 460",
    category=Category.LECTURE_HALL,
    year=2021,
    specialization=Specialization.INFORMATICS,
    building="ГУК",
)

AUDIENCE2 = Audience(
    id="А-404",
    name="Аудитория 404",
    category=Category.SEMINAR_ROOM,
    year=2017,
    specialization=Specialization.PHILOSOPHY,
    building="3",
)
