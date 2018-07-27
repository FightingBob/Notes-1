import random

from algorithm import binary_search, bubble_sort, flatten, select_sort, \
        insert_sort, merge_sort, quick_sort, quick_sort_inplace, partition, \
        k_most


def test_flatten():
    items = [1, 2, [1], [], [1, 2, 3]]
    assert flatten(items) == [1, 2, 1, 1, 2, 3]


def test_binary_search():
    items = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert binary_search(items, 0, len(items), 1) == 0
    assert binary_search(items, 0, len(items), 8) == 6
    assert binary_search(items, 0, len(items), 7) == -1

    a = list(range(10))
    for i in a:
        assert binary_search(a, 0, len(a), i) == i

    assert binary_search(a, 0, len(a), -1) == -1
    assert binary_search(a, 0, len(a), 10) == -1


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
    assert seq == sorted(seq)


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
    assert seq == sorted(seq)


def test_insert_sort():
    seq = list(range(10))
    random.shuffle(seq)
    insert_sort(seq)
    assert seq == sorted(seq)


def test_merge_sort():
    seq = list(range(10))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)
    seq = []
    assert merge_sort(seq) == []


def test_quick_sort():
    seq = list(range(10))
    random.shuffle(seq)
    assert quick_sort(seq) == sorted(seq)
    seq = []
    assert merge_sort(seq) == []


def test_partition():
    seq = [2, 1, 0, 4]
    assert partition(seq, 0, len(seq)) == 2
    seq = [1, 2, 3, 4]
    assert partition(seq, 0, len(seq)) == 0
    seq = [4, 3, 2, 1]
    assert partition(seq, 0, len(seq)) == 3


def test_quick_sort_inplace():
    seq = list(range(10))
    random.shuffle(seq)
    quick_sort_inplace(seq, 0, len(seq))
    seq = list(range(-2, 10))
    random.shuffle(seq)
    quick_sort_inplace(seq, 0, len(seq))
    seq = list(range(100))
    random.shuffle(seq)
    quick_sort_inplace(seq, 0, len(seq))
    assert seq == sorted(seq)
    seq = []
    quick_sort_inplace(seq, 0, len(seq))
    assert seq == []


def test_k_most():
    seq = list(range(10))
    random.shuffle(seq)
    assert k_most(seq, 7) == 6
