from typing import List, Union

def multiply_list(data: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    """Умножает каждый элемент списка на заданный множитель."""
    return [item * multiplier for item in data]


def main():
    input_str = input("Введите список чисел через пробел: ")
    try:
        data = [float(x) for x in input_str.split()]
    except ValueError:
        print("Неверный формат ввода списка.")
        return

    try:
        multiplier_str = input("Введите множитель (по умолчанию 2): ")
        if multiplier_str:
            multiplier = float(multiplier_str)
        else:
            multiplier = 2
    except ValueError:
        print("Неверный формат ввода множителя.")
        return

    result_func = multiply_list(data, multiplier)
    result_lambda = list(map(lambda x: x * multiplier, data))

    print("Результат (функция):", result_func)
    print("Результат (лямбда-функция):", result_lambda)


if __name__ == "__main__":
    main()

