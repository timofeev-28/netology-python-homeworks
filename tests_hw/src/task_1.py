def check_month(month: int) -> str:
    """accepts the ordinal number of the month and returns the time of the year"""
    if month in (12, 1, 2):
        season = "Зима"
    elif month in (3, 4, 5):
        season = "Весна"
    elif month in (6, 7, 8):
        season = "Лето"
    elif month in (9, 10, 11):
        season = "Осень"
    else:
        season = "Некорректный номер месяца"
    return season
