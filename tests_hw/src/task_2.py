def get_cost(weight: int):
    if not isinstance(weight, int) or weight <= 0:
        raise ValueError("Проверьте массу посылки")
    if 0 < weight <= 10:
        return "Стоимость доставки: 200 руб."
    if weight > 10:
        return "Стоимость доставки: 500 руб."
