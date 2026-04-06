from datetime import datetime
from functools import wraps


def logger(path):
    """decorator writes to the file the date and time of the
    function call, the name of the function, the arguments with which
    it was called, and the return value, the path to the file is passed
    in the arguments of the decorator
    """

    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = (
                f"{start_time} - "
                f"функция: {old_function.__name__}, "
                f"аргументы: args={args}, kwargs={kwargs}, "
                f"результат: {result}\n"
            )
            with open(path, "a", encoding="utf-8") as f:
                f.write(f"{log_entry}")
            return result

        return new_function

    return __logger
