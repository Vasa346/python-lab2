#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Task1:
    """
    Задача 1 (Вариант 8)
    Сколько существует последовательностей длины 6 в алфавите {К, А, Т, Е, Р},
    начинающихся с Р и заканчивающихся на К.
    """

    def __init__(self):
        self.result = None

    def solve(self):
        """Вычисляет количество последовательностей."""
        # Алфавит: К, А, Т, Е, Р (5 букв)
        # Длина последовательности: 6
        # Первая буква: Р (1 вариант)
        # Последняя буква: К (1 вариант)
        # Средние 4 позиции: любая из 5 букв
        count = 1 * (5**4) * 1
        self.result = count
        return self.result

    def run_tests(self):
        """
        Доктесты для проверки решения.
        >>> t = Task1()
        >>> t.solve()
        625
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    task = Task1()
    print(task.solve())
