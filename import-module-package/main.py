from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from application.use_numpy import use_numpy


if __name__ == "__main__":
    print(f"Текущая дата: {datetime.now().date()}")
    calculate_salary()
    get_employees()
    use_numpy()
