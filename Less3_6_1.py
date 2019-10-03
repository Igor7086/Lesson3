def ent_num():
    while True:
        number = input("Enter number: ")
        try:
            number = float(number)
        except ValueError:
            pass
        else:
            break
    return number


print(ent_num())



