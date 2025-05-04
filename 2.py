import math
import statistics

def addition(x: float, y: float) -> float:
    return x + y

def subtraction(x: float, y: float) -> float:
    return x - y

def multiplication(x: float, y: float) -> float:
    return x * y

def division(x: float, y: float) -> Union[float, str]:
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    choice = input("Выберите тип деления (1 - обычное, 2 - остаток, 3 - нацело): ")
    if choice == '1':
        return x / y
    elif choice == '2':
        return x % y
    elif choice == '3':
        return x // y
    else:
        raise ValueError("Неверный выбор типа деления")


def exponentiation(x: float, y: float) -> float:
    return x ** y

def factorial(x: int) -> int:
    if not isinstance(x, int) or x < 0:
        raise TypeError("Факториал определен только для неотрицательных целых чисел")
    return math.factorial(x)

def sine(x: float) -> float:
    return math.sin(x)

def median(data: list) -> float:
    if not isinstance(data, list):
        raise TypeError("Для медианы требуется список чисел")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("Список должен содержать только числа")

    return statistics.median(data)


def main():
    while True:
        print("Доступные операции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Синус")
        print("8. Медиана")
        print("--------------------")

        operation = input("Операция (или 'exit' для выхода): ")

        if operation.lower() == 'exit':
            break

        try:
            operation = int(operation)
            if not 1 <= operation <= 8:
                raise ValueError
        except ValueError:
            print("Неверный номер операции.")
            continue

        try:
            if operation in [1, 2, 3, 4, 5]:
                x = float(input("Операнд 1: "))
                y = float(input("Операнд 2: "))
                if operation == 1:
                    result = addition(x, y)
                elif operation == 2:
                    result = subtraction(x, y)
                elif operation == 3:
                    result = multiplication(x, y)
                elif operation == 4:
                    result = division(x, y)
                elif operation == 5:
                    result = exponentiation(x, y)
            elif operation == 6:
                x = int(input("Число: "))
                result = factorial(x)
            elif operation == 7:
                x = float(input("Число: "))
                result = sine(x)
            elif operation == 8:
                input_str = input("Список чисел через пробел: ")
                try:
                  data = [float(x) for x in input_str.split()]
                except ValueError:
                  print("Неверный ввод списка")
                  continue
                result = median(data)
            print(">>>", result)

        except (ValueError, TypeError, ZeroDivisionError) as e:
            print(e)
        print("--------------------")

if __name__ == "__main__":
    main()
