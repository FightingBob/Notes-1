s1 = {1, 3, 2}

s2 = s1
print(s1)
print(s2)

del s1
try:
    print(s1)
except NameError:
    print("s1 not define")
print(s2)

print(globals())

del s2

print('-' * 20)

print(globals())
