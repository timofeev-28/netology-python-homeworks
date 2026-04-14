import pytest
from src.task_2 import get_cost


@pytest.mark.parametrize(
    "weight, expected",
    (
        (6, "200"),
        (10, "200"),
        (11, "500"),
        (400, "500"),
    ),
)
def test_get_cost(weight: int, expected: str):
    result = get_cost(weight)
    assert (
        expected in result
    ), f"Стоимость доставки должна быть {expected} руб. если вес {weight} кг"


@pytest.mark.parametrize(
    "invalid_weight",
    [0, -5, None, [], {}, "1"],
)
def test_calculate_get_cost_invalid_value(invalid_weight):
    with pytest.raises(ValueError):
        get_cost(invalid_weight)
