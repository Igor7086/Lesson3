from Lesson3.Less3_6_4 import triangle


def what_triangle(a, b, c):
    if triangle(a, b, c) is True:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or a == c:
            return "Isosceles triangle "
        else:
            return "Versatile triangle "
    else:
        return "Not a triangle"


print(what_triangle(7, 7, 2))
