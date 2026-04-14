import pytest
from src.api_yd import create_folder_yd, is_folder_yd, delete_folder


folder: str = "test"
success = 201
folder_exists = 409

# если папка есть на ЯндексДиске - удаляем
if is_folder_yd("/", folder):
    delete_folder(folder)


def test_create_folder_yd_success():
    result: int = create_folder_yd(folder)
    assert (
        result == success
    ), f"Ошибка при создании папки, ожидалось '201', а получено {result}"


def test_is_folder_yd():
    result: bool = is_folder_yd("/", folder)
    assert result, f"Папка {folder} отсутствует на ЯндексДиске"


def test_create_folder_yd_folder_exists():
    """Когда папка уже есть на ЯндексДиске"""
    result: int = create_folder_yd(folder)
    assert (
        result == folder_exists
    ), f'Ошибка, если папка уже есть, ожидается 409, а получено "{result}"'
