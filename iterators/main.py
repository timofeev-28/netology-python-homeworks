from src.flat_gen_any import test_4
from src.flat_iterator import test_1
from src.flat_generator import test_2
from src.flat_iter_any import test_3


if __name__ == "__main__":
    try:
        test_1()
        test_2()
        test_3()
        test_4()
    except TypeError as e:
        print(f"Ой, ошибка: {e}")
