num = int(input("Введите число: "))
i = 0
while num % 2 != 1:
    num /= 2
    i += 1
print(num, i)
