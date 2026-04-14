from src.task_3 import check_auth


def test_correct_login_and_password():
    assert check_auth("admin", "password") == "Добро пожаловать"


def test_wrong_login_and_password():
    assert check_auth("zzz", "abc") == "Доступ ограничен"


def test_wrong_login():
    assert check_auth("xxx", "password") == "Доступ ограничен"


def test_wrong_password():
    assert check_auth("admin", "abc") == "Доступ ограничен"


def test_invalid_arguments():
    assert check_auth([], None) == "Доступ ограничен"
