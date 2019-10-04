a = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)"""

b = a.split()
c = []
num = len(b)

for i in range(num):
    c.append(b[i].strip('!' '(' ')' '"' '-' '_' ',' '.' ':' ';' '/' '?').lower())

c.sort()
print('количество слов в тексте: ', num)
print(c)






