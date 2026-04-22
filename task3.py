#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Task3:
    """
    Задача 3 (Вариант 8)
    Найти числа, соответствующие маске 12345?7?8, делящиеся на 23.
    Вывести число и результат деления на 23.
    """

    def __init__(self):
        self.results = []

    def solve(self):
        """Находит числа по маске 12345?7?8, кратные 23."""
        self.results = []
        for d1 in range(10):
            for d2 in range(10):
                num = int(f"12345{d1}7{d2}8")
                if num % 23 == 0:
                    self.results.append((num, num // 23))
        self.results.sort()
        return self.results

    def run_tests(self):
        """
        Доктесты для проверки решения.
        >>> t = Task3()
        >>> t.solve()
        [(123450798, 5367426), (123451718, 5367466), (123453788, 5367556), (123454708, 5367596), (123456778, 5367686), (123459768, 5367816)]
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    task = Task3()
    results = task.solve()
    for num, div in results:
        print(num, div)
