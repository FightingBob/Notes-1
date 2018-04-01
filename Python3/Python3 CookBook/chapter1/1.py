from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
            # line 为存在 'python' 的那一行
            # previous_lines 为 存在 python的前面5行 或5行以下
        previous_lines.append(line)


if __name__ == '__main__':
    with open('1.txt') as f:
        for line, previous in search(f, 'python', 5):
            for pline in previous:
                print(pline, end="")
            print(line, end="")
            print("-" * 20)
