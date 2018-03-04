

# if len(middle) is too many it should be get a error "too many values to unpack(解压缩)"
def filter_first_and_last(s):
    first, *middle, last = s
    print(first, middle, last)


# user the * can solve some thing are practial
def get_args(ss):
    for tag, *args in recods:
        if tag == 'foo':
            print(*args)
        else:
            print('no')
    



if __name__ == "__main__":
    words = "HELLO"
    recods = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
    ]
    filter_first_and_last(words)
    get_args(recods)
    