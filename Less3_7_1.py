a = """We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)"""


b = a.split()
c = []
num = len(b)
# i = 0

for i in b:
    c.append(i.strip('!()"-_,.:;?').lower())

c.sort()
print('количество слов в тексте: ', num)
print(c)

comp = {}
co = 1
for i in range(num):
    comp[c[i]] = c.count(c[i])

print(comp)




