try:
    s = input("Введите строку: ")
    print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2],
      s[-2::-2], s[-2:0:-1], len(s), sep="\n")
except IndexError:
    print("enter error")



