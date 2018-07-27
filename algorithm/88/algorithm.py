def rescursion(n):
    """尾递归"""
    if n > 0:
        print(n)
        rescursion(n-1)


def flatten(l):
    """列表扁平化
    [1,[1,2],[]] -> [1,2,2]
    """
    result = []

    def nerd(l):
        for item in l:
            if not isinstance(item, list):
                result.append(item)
            else:
                nerd(item)
    nerd(l)
    return result


def hannot(n, f, buffer, t):
    """汉罗塔
    @params f: from
    @params buffer
    @params t: to
    """
    if n == 1:
        print(f, '--->', t)
    else:
        hannot(n-1, f, t, buffer)
        hannot(1, f, buffer, t)
        hannot(n-1, buffer, f, t)


"""
if __name__ == "__main__":
    hannot(1, 'a', 'b', 'c')
    print('-'*10)
    hannot(2, 'a', 'b', 'c')
    print('-'*10)
    hannot(3, 'a', 'b', 'c')
    print('-'*10)
    hannot(5, 'a', 'b', 'c')
"""


def binary_search(array, beg, end, val):
    """递归二分查找"""
    if beg >= end:
        return -1
    else:
        mid = (beg + end) // 2
        if array[mid] == val:
            return mid
        elif array[mid] > val:
            return binary_search(array, beg, mid, val)
        else:
            return binary_search(array, mid+1, end, val)


def bubble_sort(array):
    """冒泡排序"""
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def select_sort(array):
    """选择排序"""
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]


def insert_sort(array):
    """插入排序"""
    n = len(array)
    for i in range(1, n):
        value = array[i]
        pos = i
        while pos > 0 and value < array[pos-1]:
            array[pos] = array[pos-1]
            pos -= 1
        array[pos] = value


def merge_sort(seq):
    """归并排序 是返回一个新的序列"""
    if len(seq) <= 1:
        return seq
    else:
        mid = len(seq) // 2
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])

        new_seq = merge_sroted_list(left_half, right_half)
        return new_seq


def merge_sroted_list(left_half, right_half):
    """将两个排好序的序列合并成一个排好序的序列"""
    length_a, length_b = len(left_half), len(right_half)
    a = b = 0
    new_seq = list()
    while a < length_a and b < length_b:
        if left_half[a] >= right_half[b]:
            new_seq.append(right_half[b])
            b += 1
        else:
            new_seq.append(left_half[a])
            a += 1

    while a < length_a:
        new_seq.append(left_half[a])
        a += 1

    while b < length_b:
        new_seq.append(right_half[b])
        b += 1

    return new_seq


def quick_sort(seq):
    """粗劣版本的快速排序"""
    if len(seq) <= 1:
        return seq
    else:
        pivot_index = 0
        pivot_value = seq[pivot_index]
        less_part = [i for i in seq[pivot_index+1:] if i <= pivot_value]
        great_part = [i for i in seq[pivot_index+1:] if i > pivot_value]
        return quick_sort(less_part) + [pivot_value] + quick_sort(great_part)


def partition(seq, beg, end):
    pivot_index = beg
    pivot = seq[beg]
    left = beg + 1
    right = end - 1
    while True:
        while left <= right and seq[left] < pivot:
            left += 1

        while left <= right and seq[right] >= pivot:
            right -= 1

        if left > right:
            break

        else:
            seq[left], seq[right] = seq[right], seq[left]

    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    return right


def quick_sort_inplace(seq, beg, end):
    """快速排序 左闭右开
    like range
    [1, 2)
    """
    if beg < end:
        pivot = partition(seq, beg, end)
        quick_sort_inplace(seq, beg, pivot)
        quick_sort_inplace(seq, pivot+1, end)


def k_most(seq, k):
    for i in range(len(seq)):
        pivot = partition(seq, 0, len(seq))
        if seq[pivot] == k-1:
            return seq[pivot]
        else:
            seq[0], seq[i+1] = seq[i+1], seq[0]
