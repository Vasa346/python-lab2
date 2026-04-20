#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Task1:
    """
    Задача 1 (Вариант 8)
    Сколько единиц содержится в двоичной записи значения выражения:
    8**2020 + 4**2017 + 26 - 1
    """

    def __init__(self):
        self.result = None

    def solve(self):
        """Вычисляет количество единиц в двоичной записи."""
        value = 8**2020 + 4**2017 + 26 - 1
        binary = bin(value)
        self.result = binary.count('1')
        return self.result

    def run_tests(self):
        """
        Доктесты для проверки решения.
        >>> t = Task1()
        >>> t.solve()
        5
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    task = Task1()
    print(task.solve())