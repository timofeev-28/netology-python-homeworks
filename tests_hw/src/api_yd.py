import os
import requests
from dotenv import load_dotenv


load_dotenv()
TOKEN_YD = os.getenv("YD_TOKEN")
URL: str = "https://cloud-api.yandex.net/v1/disk/resources"
HEADERS: dict = {"Authorization": f"OAuth {TOKEN_YD}"}


def create_folder_yd(folder: str) -> int:
    """Cоздаёт папку на ЯндексДиске"""

    params: dict = {"path": folder}
    try:
        response = requests.put(URL, headers=HEADERS, params=params)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")
    return response.status_code


def is_folder_yd(folder: str, check_folder: str) -> bool:
    """
    Проверяет наличие папки wanted_folder в корневой директории ЯндексДиска
    """
    params: dict = {"path": folder}
    try:
        response = requests.get(URL, headers=HEADERS, params=params)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")

    folders: list = []
    for item in response.json()["_embedded"]["items"]:
        folders.append(item["name"])
    return check_folder in folders


def delete_folder(folder):
    """удаляет папку с ЯндексДиска минуя корзину"""
    requests.delete(
        URL,
        headers=HEADERS,
        params={"path": folder, "permanently": True},
    )
