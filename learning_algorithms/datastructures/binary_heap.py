"""
Covers topics from

https://www.notion.so/ammul/Queues-c6eafab37eb7480da05607c89c4e28f2
https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#96b4e496656543beb18567aef7f24b4d

around priority queue using binary heap
"""
import math
from typing import List


def example1_binary_tree():
	"""
	"Example1-BT" in https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#917515359872405a9cd0d9dac39b903a

	"""
	g = "a,b,c,d,e,f,g".split(",")
	n = len(g)
	print(g, n)
	print([str(i) for i in range(n)])
	for i in range(n):
		e = g[i]
		parent, leftchild, rightchild = get_parent_leftchild_rightchild_from_binary_tree(n, g, i)
		print(f"g[{i}]={e}; parent: {parent}; leftchild: {leftchild}; rightchild: {rightchild}")


def get_parent_leftchild_rightchild_from_binary_tree(n, g, i):
	"""Small utility to get  (parent, leftchild, rightchild) nodes
	for given binary tree g and index i

	NOTE: This follows "BINARYTREERULE" as described in https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#917515359872405a9cd0d9dac39b903a

	Args:
		n: int: size of g
		g: list: array representing binary graph
		i: int: index for which we have to find related nodes
	"""
	parenti = math.floor((i-1)/2)
	parent = g[parenti] if parenti >= 0 else None
	leftchildi = 2*i+1
	leftchild = g[leftchildi] if leftchildi < n else None
	rightchildi = 2*i+2
	rightchild = g[rightchildi] if rightchildi < n else None
	return (parent, leftchild, rightchild)


class MinBinaryHeapPQ:
	"""This class represents a Minimum Priority Queue
	built using min-heap (minimum binary heap)

	https://www.youtube.com/watch?v=GLIRnUhknP0&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=18
	almost replica of java version: https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/priorityqueue/BinaryHeap.java
	"""
	def __init__(self):
		# Binary Graph representation as an List/Array
		self._heap = []

	@classmethod
	def from_heapify(cls, elems):
		"""Heapify way to create queue using O(n)
		"""
		pass

	@classmethod
	def from_regular(cls, elems):
		"""Regular way to create queue using O(nlogn)
		"""
		pass

	def is_empty(self):
		return self.size() == 0
	
	def size(self):
		return len(self._heap)
	
	def clear(self):
		n = self.size()
		for i in range(n):
			self._heap[i] = None
	
	def peek(self):
		if self.is_empty(): return None
		return self._heap[0]
	
	def poll(self):	# remove root (O(logn))
		return self.remove_at(0)
	
	def contains(self, elem) -> bool:
		n = self.size()
		for i in range(n):
			if self._heap[i] == elem: return True
		return False

	def add(self, elem):
		"""Insert operation to Heap

		Logic: same as "Insert Operation in Max Heap" in https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#e1b277d95fd144df8d6cb0b0804f8935
		only difference is this is for min-heap:
		1. add elem to the end to maintain binary tree (INSERTRULE1.1)
		2. move the elem from leaf to root to maintain min heap condition (swim) (INSERTRULE1.2)
		"""
		if elem is None: raise Exception("elem cannot be none since we expect only non-null values")
		# 1. add elem to the end to maintain binary tree
		self._heap.append(elem)
		# 2. move elem from leaf -> root. i.e. swim from index of elem (i.e. last elem)
		self._swim(self.size() - 1)
	
	def _swim(self, k):
		"""Move given elem's index from leaf -> root (bottom up) by following logic:
		if k's elem (assuming currently at leaf) < parent, swap
		repeat until k is swapped all the way to the top if needed
		This takes O(logn) time
		"""
		l = self._heap	# list
		# NOTE: k is 0-indexed, hence using following rule
		parent = math.floor((k-1)/2)	# parent's index

		# if we haven't reached the root (root is at k==0) and
		# parent is bigger (in a min-heap, parent is smaller),
		# swap k to swim from leaf to root:
		while (k > 0 and l[k] < l[parent]):
			# since k is bigger
			self._swap(parent, k)	# changes the elem values with position
			k = parent	# k is now the parent
			# new parent
			parent = math.floor((k-1)/2)	# parent's index

	def _swap(self, i, j): # swap i with j
		tmpi = self._heap[i]
		self._heap[i] = self._heap[j]
		self._heap[j] = tmpi

	def is_min_heap(self, k: int=0) -> bool:
		"""
		Recursively check if heap is a min Heap, starting from root
		Returns True if min heap

		Logic:
		1. since this function accepts k as an index,
		check wrt k index if parent is smaller than its children.
		if smaller, visit left and right children
		"""
		# if we have reached the end of the heap, stop
		# and return true, since all below conditions were met, so its a min heap
		l = self._heap
		n = self.size()
		if k >= n: return True

		# k is parent, so find its children indexes
		# NOTE: k is 0-indexed, hence using following rules
		left = 2*k + 1
		right = 2*k + 2

		# if parent found bigger than child, return false
		if left < n and l[k] > l[left]:
			return False
		if right < n and l[k] > l[right]:
			return False
		
		# for given k, parent and child satified min-heap condition, so traverse children
		# where in next recursion, children become parents
		# and return True if both left and right children's childrens satify the conditions
		return self.is_min_heap(left) and self.is_min_heap(right)

	def remove(self, elem):
		"""Remove given elem

		We follow same logic as described in "Delete Operation in Max Heap"
		https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#010350ee1d884fa1bbdeaa3e6860e66a
		1. delete the root first by swapping last elem with root (DELETERULE1.1)
		2. sink from root to leaf to maintain the min-heap (DELETERULE1.2)
		NOTE: the root here is actually the given elem, not the actual root of heap
		so basically we are work on a sub-heap if given elem != actual root
		"""
		if elem == None: return False
		# Linear removal - O(n)
		for i in range(self.size()):
			if self._heap[i] == elem:
				self._remove_at(i)
				return True
		return False

	def _remove_at(self, i):	# remove node in an index (O(logn))
		if self.is_empty(): return None
		# before swapping, store current i's val so that we can return it
		original_val = self._heap[i]

		# as per DELETERULE1.1:
		# move root (i) to the bottom and bring last elem to the top
		last_elem = self.size() - 1
		last_elem_val = self._heap[last_elem]
		self._swap(i, last_elem)
		# delete the removed elem from heap
		self._heap.pop(last_elem)
		# if last elem removed, return
		if i == last_elem: return original_val

		# as per DELETERULE1.2, sink last_elem (now root) to bottom
		self._sink(i)

		# Since we might be removing elem from middle of the heap,
		# we have to also try swimming up to maintain min-heap
		if self._heap[i] == last_elem_val:	# sink didn't change anything
			self._swim(i)
		
		return original_val
	
	def _sink(self, k):
		"""Move given elem's index from root -> leaf (top down) by following logic:
		if k's elem (assuming currently at root) > smallest children, swap
		repeat until k is swapped all the way to the bottom if needed
		This takes O(logn) time
		"""
		l = self._heap
		n = self.size()

		while True:
			# calculate children indexes
			left = 2*k + 1
			right = 2*k + 2
			# find smallest child
			smallestchild = left
			# NOTE: we only need "right < n" because right > left
			if right < n and l[smallestchild] > l[right]:
				smallestchild = right
			
			# if given elem is less than smallest child or
			# we have reached end of the heap, stop
			# NOTE: we need "smallestchild >= n" check first otherwise we will get IndexError
			if smallestchild >= n or l[k] < l[smallestchild]:
				break
			
			# given elem is bigger than smallest child
			self._swap(k, smallestchild)
			k = smallestchild	# navigate to smallest child


def main():
	# example1_binary_tree()
	q = MinBinaryHeapPQ()
	q.add(30)
	q.add(1)
	q.add(20)
	q.add(10)
	q.add(30)
	q.add(5)
	q.add(11)
	q.remove(10)
	q.remove(30)
	print(q._heap)
	assert q.is_min_heap() == True

main()
