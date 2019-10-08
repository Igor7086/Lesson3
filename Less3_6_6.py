
def distance(x1, y1, x2, y2):
    from math import sqrt
    xy = sqrt((x2 - x1)**2 +(y2 - y1)**2)
    return xy


print(distance(float(input("Введите x1: ")),
               float(input("Введите y1: ")),
               float(input("Введите x2: ")),
               float(input("Введите y2: "))))

