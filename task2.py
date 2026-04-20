#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Task2:
    """
    Задача 2 (Вариант 8)
    Найти простые числа в диапазоне [245690; 245756].
    Вывести порядковый номер и число.
    """

    def __init__(self):
        self.primes = []

    @staticmethod
    def is_prime(n):
        """Проверка на простоту."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def solve(self):
        """Находит все простые числа в заданном диапазоне."""
        self.primes = []
        for num in range(245690, 245757):
            if self.is_prime(num):
                self.primes.append(num)
        return self.primes

    def run_tests(self):
        """
        Доктесты для проверки решения.
        >>> t = Task2()
        >>> t.solve()
        [245711, 245719, 245723, 245741, 245747, 245753]
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    task = Task2()
    primes = task.solve()
    for i, p in enumerate(primes, start=1):
        print(i, p)