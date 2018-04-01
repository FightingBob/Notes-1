# 字符串开头或结尾匹配

filename = "a.txt"

print(filename.endswith('.txt'))
print(filename.startswith('a'))

# 多种可能

print(filename.endswith(('.txt', '.jpg', '.png')))

# 注意 传入的列表必须为元祖

try:
    print(filename.startswith(['a', 'b', 'c']))
except TypeError:
    pass
