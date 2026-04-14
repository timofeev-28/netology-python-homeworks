def check_auth(login: str, password: str):

    if login == "admin" and password == "password":
        return "Добро пожаловать"

    return "Доступ ограничен"
