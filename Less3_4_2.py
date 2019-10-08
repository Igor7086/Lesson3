"""
st = 'qwerty'
i = 0
while i <= len(st):
    st1 = st[i:]
    print(st1)
    i += 1
"""
st = 'qwerty'
while st:
    st = st[1:]
    print(st)

