

p = [1, 3]
x, y = p

print(x, y)


date = ["a", 50, 8.0, (212, 12, 11)]
a, b, c, d = date

print(a, b, c, d)

a, b, c, (x, y, z) = date

print(a, b, c, d)
print(x, y, z)

"""
p = [1, 2, 3]
x, y = p

if you do like this 
you must be get a error about ValuError 
"""

"""
just x can iteration
you can use this way
"""
s = "hello"
a, b, c, d, e = s

print(a, b, c, d, e)

# if you don't want  variables


_, b, c, d, _= s
print(b, c, d)

# make sure _ you cann't use