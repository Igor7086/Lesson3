def triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False


print(triangle(int(input("Введите 1ю сторону: ")),
               int(input("Введите 2ю сторону: ")),
               int(input("Введите 3ю сторону: "))))


