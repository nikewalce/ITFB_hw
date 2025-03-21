"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    >>> power_numbers(-10, -5, 0, 1, 2, 5, 7, 10, 11)
    [100, 25, 0, 1, 4, 25, 49, 100, 121]
    """
    return [num**2 for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num: int) -> bool:
    """Функция для проверки одного числа, простое ли это число
    (Функция is_prime принимает одно число и возвращает True, когда число простое и False, когда нет)"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_numbers(num_lst: list, filter_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([-3, -2, 0, 1, 2, 3, 7], ODD)
    [-3, 1, 3, 7]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    >>> filter_numbers([-4, 0, 2, 3, 4, 5, 8], EVEN)
    [-4, 0, 2, 4, 8]
    >>> filter_numbers([2, 3, 4, 5], PRIME)
    [2, 3, 5]
    >>> filter_numbers([-7, 0, 2, 3, 4, 5, 6, 7], PRIME)
    [2, 3, 5, 7]
    """
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 != 0, num_lst))
    elif filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, num_lst))
    elif filter_type == PRIME:
        return list(filter(is_prime, num_lst))
    else:
        raise ValueError("Неверный тип фильтра")
