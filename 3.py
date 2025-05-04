from typing import List, Union, Any

def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Args:
        search: Строка, определяющая тип обработки ("args" или "kwargs").
        status: Булево значение, определяющее условия обработки для "args".
        *args: Позиционные аргументы.
        **kwargs: Именованные аргументы.

    Returns:
        Список целых чисел, если search == "args" и status == True.
        Строка, если search == "args" и status == False, или если search == "kwargs".

    Raises:
        ValueError: Если search не равен "args" или "kwargs".
    """
    result: List[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")


