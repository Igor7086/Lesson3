a1 = input('введите первое значение:')
a2 = input('введите второе значение:')
try:
    print(float(a1) + float(a2))
except ValueError:
    print(a1+a2)



