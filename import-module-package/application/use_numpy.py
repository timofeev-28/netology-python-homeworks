import numpy as np


def use_numpy() -> None:
    arr = np.array([1, 2, 3, 4, 5])
    print("\n==== Использование библиотеки numpy ====")
    print("Исходный массив:", arr)
    print("Среднее значение:", np.mean(arr))
    print("Сумма элементов:", np.sum(arr))
