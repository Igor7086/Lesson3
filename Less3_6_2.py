def ent_word():
    while True:
        try:
            word = input("Введите слово:").strip()
        except ValueError:
            pass
        else:
            if ' ' not in word:
                break
    return word


print(ent_word())



