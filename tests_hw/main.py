from src.api_yd import create_folder_yd, is_folder_yd
from src.task_1 import check_month
from src.task_2 import get_cost
from src.task_3 import check_auth


if __name__ == "__main__":
    try:
        print(check_month(10))
        print(get_cost(3))
        print(check_auth("admin", "password"))
        print(create_folder_yd("test"))
        print(is_folder_yd("/", "test"))
    except ValueError as e:
        print(f"WARN: {e}")
