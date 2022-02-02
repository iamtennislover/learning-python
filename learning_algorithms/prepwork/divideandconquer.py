
def is_list_sorted_recursive(l, i=0):
	"""
	Goal: Check if list/array is sorted or not.

	Logic:
		Basic idea is any nth elem will need to be larger than n-1th elem
		for the list to be sorted.
		Using recursion, divide given list into smallest possible list
		containing only two elems.
		Then compare two elems.
		pseudo-code:
			for given ith elem,
			if l[i] less than l[i+1], try next i
			else stop return false
			i must be < n
		Base condition: if i reaches the end, we have gone through entire list so list must be sorted

	Time: O(n)
	Strategy: divide and conquer

	Ref: https://www.geeksforgeeks.org/program-check-array-sorted-not-iterative-recursive/
	"""
	n = len(l)
	j = i + 1
	if j >= n:	# base condition
		# this means, i have reached end of list, so i must be sorted, so return True
		return True
	
	if l[i] > l[j]:
		return False
	return is_list_sorted_recursive(l, j)


def is_list_sorted_iterative(l):
	"""
	Goal: Same as is_list_sorted_recursive, but use iteration
	pseudo-code:
		for i iterate until n:
			if l[i] > l[i+1]: return False
	"""
	n = len(l)
	for i in range(n):
		j = i+1
		if j >= n:
			break
		if l[i] > l[j]:
			return False
	return True


def binary_search_recursion(l, x, il=None, ir=None):
	"""
	Goal: search an elem (x) in sorted list (l) in O(logn) time (binary search)
	and return the index. if not found, return -1

	Time: O(logn)
	Strategy: divide and conquer using recursion

	Logic:
		Basic idea is that since list is already sorted, we can safely
		assume that when we split the list into two halfs, x will be
		present in left half if x <= middle, else x will be present in right half.
		Repeat until we have found it
		Base condition: if our indexes go out of bound or left index (il) > right index (ir)
		Pseudo-code:
			[10,20,30,40,50,60,70,80,90,100]
			m = n/2 # (il+ir)/2
			if x == l[m]:
				return m
			if x < l[m]:
				il = 0
				ir = m + 1
			else:
				il = m + 1
				ir = n
			return -1 if il >= ir
			recurse on list from il to ir, with n=il+ir
	"""
	if il == ir == None:	# initialize for first iteration
		il = 0; ir = len(l) - 1
	m = int((il+ir)/2)
	# print(f"il={il} m={m} ir={ir}")
	if il > ir:	# base condition
		return -1
	if x == l[m]:
		return m
	if x < l[m]:
		return binary_search_recursion(l,x,il,m-1)
	return binary_search_recursion(l,x,m+1,ir)


def binary_search_iteration(l, x):
	"""Goal: Same as binary_search_recursion, but using iteration

	Pseudo-code:
		Which loop to use? - could use for or while, but idea remains the same:
		find middle index from left and right
		if x == l[m]: found
		if x < l[m]:
			left remains the same
			right = m - 1
		else:
			left = m + 1
			right remains the same
	We can iterate using for loop since the time it will take is <O(n),
	but its more readable and clear if we use while, where while left < right
	"""
	left = 0
	right = len(l) - 1
	while left <= right:
		mid = int((left + right)/2)
		# print(f"left={left} mid={mid} right={right}")
		if x == l[mid]:
			return mid
		if x < l[mid]:
			right = mid - 1
		if x > l[mid]:
			left = mid + 1
	return -1


def test_is_list_sorted():
	testcases = [
		# list, result
		([2,3,4], True),
		([1,5,10,11], True),
		([1,1,10,10], True),
		([11,1,10,10], False),
		([1,2,3,0], False),
		([1,2,0], False),
		([1], True),
	]
	for t in testcases:
		r = is_list_sorted_recursive(t[0])
		assert r == t[1]
		r = is_list_sorted_iterative(t[0])
		assert r == t[1]


def test_binary_search():
	testcases = [
		# list, x, expected
		([2], 1, -1),
		([2], 3, -1),
		([2], 2, 0),
		([2,3,4], 1, -1),
		([2,3,4], 5, -1),
		([2,3,4], 2, 0),
		([2,3,4], 3, 1),
		([2,3,4], 4, 2),
		([0,10,20,30,40,50,60,70,80,90], 60, 6),
		([0,10,20,30,40,50,60,70,80,90], 100, -1),
	]
	for t in testcases:
		# print(t)
		r = binary_search_recursion(t[0], t[1])
		assert r == t[2]
		r = binary_search_iteration(t[0], t[1])
		assert r == t[2]


def main():
	test_is_list_sorted()
	test_binary_search()

main()