"""
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние
между точкой (x1, y1) и (x2, y2). Считайте четыре действительных
числа от пользователя и выведите результат работы этой функции.
"""


def distance(x1, y1, x2, y2):
    from math import sqrt
    x1y1 = sqrt(x1**2 + y1**2)
    x2y2 = sqrt(x2**2 + y2**2)
    return x1y1, x2y2


print(distance(float(input("Введите x1: ")),
               float(input("Введите y1: ")),
               float(input("Введите x2: ")),
               float(input("Введите y2: "))))

