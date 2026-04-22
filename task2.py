#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Task2:
    """
    Задача 2 (Вариант 8)
    Значение выражения 216^6 + 216^4 + 36^6 - 6^14 - 24 записали в системе с основанием 6.
    Сколько различных цифр содержит эта запись?
    """

    def __init__(self):
        self.result = None

    def solve(self):
        """Вычисляет количество различных цифр в шестеричной записи."""
        # Приводим все к основанию 6
        # 216 = 6^3
        # 36 = 6^2
        value = (6**3)**6 + (6**3)**4 + (6**2)**6 - 6**14 - 24
        # value = 6^18 + 6^12 + 6^12 - 6^14 - 24
        # value = 6^18 - 6^14 + 2 * 6^12 - 24

        # Переводим в шестеричную систему
        digits = set()
        n = value
        while n > 0:
            digits.add(n % 6)
            n //= 6
        self.result = len(digits)
        return self.result

    def run_tests(self):
        """
        Доктесты для проверки решения.
        >>> t = Task2()
        >>> t.solve()
        4
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    task = Task2()
    print(task.solve())