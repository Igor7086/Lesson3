
num = [1, 5, 5, 5, 2, 12, 12, 9, 11, 4, 4, 4, 4, 4, 8, 7, 0]
comparing = {}
i = 0
c = 1
for i in range(len(num)-1):
    if num[i] == num[i+1]:
        c += 1
        comparing[num[i]] = c
    else:
        c = 1
print(max(comparing.values()))
""" по-моему универсальнее решение в цикле range(len(num)-1) , хотя
     можно было учесть ноль в конце
"""



