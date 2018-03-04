import heapq

nums = [1, 3, 5, 100, 10, -4]
print(max(nums))


print(heapq.nlargest(3, nums))
# find 3 max
# [100, 10, 5]


print(heapq.nsmallest(3, nums))
# find 3 min
# [-4, 1, 3]

heap = list(nums)
print(heapq.heapify(heap))
