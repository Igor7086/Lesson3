"""
Пользователь вводит строку.
Разрежьте её на две части – равные, если длина строки чётная,
а если длина строки нечётная, то длина первой части должна быть
на один символ больше. Переставьте эти две части местами,
результат запишите в новую строку и выведите на экран.
"""
st = input("Введите строку символов: ")
i = len(st)//2 + len(st) % 2
st1 = st[i:] + st[:i]
print(st1)


