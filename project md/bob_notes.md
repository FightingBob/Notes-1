# 快速排序
	def sort1(l):
	    for x in range(1,len(l)):
	        for y in range(x-1,-1,-1):
	            if l[y] > l[y+1]:
	                l[y],l[y+1] = l[y+1],l[y]


# 归并排序
	def merge_sort( li ):
	    if len(li) == 1:
	        return li
	    mid = len(li) // 2
	    left = li[:mid]
	    right = li[mid:]
	    ll = merge_sort( left )
	    rl =merge_sort( right )
	    return merge(ll , rl)
		def merge( left , right ):
		    result = []
		    while len(left)>0 and len(right)>0 :
		        if left[0] <= right[0]:
		            result.append( left.pop(0) )
		        else:
		            result.append( right.pop(0) )
		    result += left
		    result += right
		    return result