
def merge(a, b):
	"""Merge two sorted list and get back sorted list
	Time: O(n)
	Space: O(n)
	"""
	# assume given two lists are already sorted
	m = len(a); n = len(b)
	c = [None]*(m+n)	# merged sorted list
	i = 0; j = 0; k = 0
	while i < m and j < n:
		# NOTE: store 1st and increment later
		if a[i] < b[j]:
			c[k] = a[i]
			i += 1	# increment only the smaller elem's index
		else:
			c[k] = b[j]
			j += 1
		k += 1
	# iterate over both (even though only one with run since we should have completed looping over the smaller already)
	# but start from where we left off
	for x in range(i, m):
		c[k] = a[x]
		k += 1
	for x in range(j, n):
		c[k] = b[x]
		k += 1
	return c


def two_way_merge_sort_recursively(l, li=None, ri=None, n=None):
	"""sort given unsorted list and return sorted list using
	2-way merge sort logic
	Time: O(nlogn)
	Space: O(2n)

	Logic: recursively merge two sorts
	basic idea is to split the given list in half until
	its single elem and while coming back up, start merging.
	because we have merge 2 lists, we need to call itself
	twice - one on left half and other on right half and then
	merge the two halfs.
	base condition is left index > right right
	"""
	# l = unsorted list
	# n = size of given list
	# li = left index
	# ri = right index

	# initialize
	if ri == None:
		n = len(l)
		li = 0; ri = n - 1

	# print(f"two_way_merge_sort_recursively: {li}-{ri}: {l}")
	mi = (li+ri)//2 # middle index
	if li >= ri:	# base condition
		return

	two_way_merge_sort_recursively(l, li, mi, n)
	# NOTE: mi+1 because we want don't want double counting middle
	two_way_merge_sort_recursively(l, mi+1, ri, n)
	# NOTE: at the end +1 since python slicing skips last elem
	left_half = l[li:mi+1]
	right_half = l[mi+1:ri+1]
	c = merge(left_half, right_half)
	# print(f"merging: {left_half} and {right_half} = {c} => l[{li}:{ri+1}] (before {l[li:ri+1]})")
	l[li:ri+1] = c


def two_way_merge_sort_iterative(l):
	"""Same as `two_way_merge_sort_recursively`
	except its iterative.

	Logic: aka bottom-up
	since need to travel with O(logn), in reverse
	order of recursion where we were splitting list in half
	to achieve this we have increase our index to the power of 2

	https://www.geeksforgeeks.org/iterative-merge-sort/
	"""
	n = len(l)
	# simple logn iterator:
	# i = 2
	# while i < n:
	# 	print(i)
	# 	i *= 2

	p = 1
	while p < n:
		_merges_per_level(l,n,p)
		p *= 2


def _merges_per_level(l, n, p):
	"""perform merges per level

	l = list
	n = size of l
	p = represents the power (i.e. 2^1, p=1; 2^3, p=3) or level
	e.g. in l=[0,1,2,3,4]; n=5; p=1; merges: merge([0],[1]); merge([2],[3]);
	"""
	print(f"working on level: {p}")
	i = 0
	while i<n:
		li = i	# left index always starts at 0
		# right index: we want li - ri distance to always be power of 2, hence need 2*p - 1
		# NOTE: In single L1 (0th level) ri = i+1 (or i + 2^0 - 1) is enough
		ri = i + 2*p - 1
		if li >= n:	# we have reached end of array, so skip
			continue
		
		mi = (li+ri)//2
		left_half = l[li:mi+1]
		right_half = l[mi+1:ri+1]
		c = merge(l[li:mi+1], l[mi+1:ri+1])
		l[li:ri+1] = c
		print(f"{i} merged: l[{li}:{mi+1}]={left_half} and r[{mi+1}:{ri+1}]={right_half} = {c} => l[{li}:{ri+1}] (before {l[li:ri+1]})")

		# NOTE: its i+2 since we want to find in pairs (p is added since want to increment)
		# (if we increment i+=1, then we would be double counting -
		# like left=[60];right=[50] in 1st, left=[50];right=[40] 
		# for [60,50,40] instead we want [60],[50] then [40],[30])
		i = i + 2*p


def test_merge():
	testcases = [
		([1,3,3,9], [2,4,5], [1,2,3,3,4,5,9]),
		([1,2,3], [4,5], [1,2,3,4,5]),
		([1,1], [1,1], [1,1,1,1]),
		([1,9,10], [90], [1,9,10,90]),
		([90], [1,20], [1,20,90]),
		([90], [100,110], [90,100,110]),
		([10,150,200,600,900], [1,2,300,400,1000], [1,2,10,150,200,300,400,600,900,1000]),
		([-1,0,5], [-2,6], [-2,-1,0,5,6])
	]
	for a, b, expected in testcases:
		assert merge(a,b) == expected


def test_two_way_merge_sort():
	testcases = [
		[5,4,3,1],
		[5,4,0,3,1],
		[1,9,3,10,-1],
		[0,1,9,3,10,0],
	]
	for l in testcases:
		o = l[:]
		# two_way_merge_sort_recursively(l)
		two_way_merge_sort_iterative(l)
		assert l == sorted(o)


def main():
	test_merge()
	test_two_way_merge_sort()


main()