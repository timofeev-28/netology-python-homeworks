import pytest
from src.task_1 import check_month


@pytest.mark.parametrize(
    "month, expected",
    (
        (1, "Зима"),
        (2, "Зима"),
        (3, "Весна"),
        (4, "Весна"),
        (5, "Весна"),
        (6, "Лето"),
        (7, "Лето"),
        (8, "Лето"),
        (9, "Осень"),
        (10, "Осень"),
        (11, "Осень"),
        (12, "Зима"),
    ),
)
def test_check_month(month: int, expected: str):
    result = check_month(month)
    assert expected == result, (
        f"Ожидаемое значение {expected} при аргументе {month} не "
        f"соответствует полученному {result}"
    )


@pytest.mark.parametrize(
    "invalid_month",
    [0, 13, -5, 100, None, [], {}, "1"],
)
def test_check_month_invalid_value(invalid_month: int):
    result = check_month(invalid_month)
    assert result == "Некорректный номер месяца", (
        f"Для аргумента {invalid_month} ожидалась строка ошибки, "
        f"получено: {result}"
    )
