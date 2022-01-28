class SimpleQueueUsingList():
	def __init__(self):
		self._list = []
	
	def __repr__(self):
		return f"SimpleQueueUsingList:{self._list}"

	def size(self):
		return len(self._list)

	def enqueue(self, e):
		self._list.append(e)
	
	def dequeue(self):
		return self._list.pop(0)


import collections
class SimpleQueueUsingDeque():
	def __init__(self):
		self._q = collections.deque()
	
	def __repr__(self):
		return f"SimpleQueueUsingList:{self._q}"
		
	def size(self):
		return len(self._q)

	def enqueue(self, e):
		self._q.append(e)
	
	def dequeue(self):
		return self._q.popleft()	# remove from head of the queue


class SimpleQueueUsingFixedArray():
	"""
	https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/queue/ArrayQueue.java
	"""
	def __init__(self, capacity):
		self._list = [None]*(capacity)
		# pointers
		self._front = 0
		self._back = 0
	
	def __repr__(self):
		return f"SimpleQueueUsingFixedArray:{self._list}"

	def size(self):
		# we can't return simply len(self._list)
		# since we want to return specific size based on front and back pointers
		# since front increments only during popping, size is going
		# to be self._back - self._front, but when size outgrows, we need to adjust the size
		n = len(self._list)
		size = self._back + n - self._front
		size = self._adjust_index(size)
		return size

	def is_empty(self):
		return self._back == self._front

	def enqueue(self, e):	# offer
		# since we always add from the back
		self._list[self._back] = e
		# increment rear
		self._back += 1
		self._back = self._adjust_index(self._back)
	
	def dequeue(self):	# pop
		# since we want fixed size, don't reduce size, simply return from top
		e = self._list[self._front]
		self._list[self._front] = None # remove it
		self._front += 1
		self._front = self._adjust_index(self._front)
		return e
	
	def _adjust_index(self, i):
		# ensure that index stays within size - i.e. loops back
		n = len(self._list)
		if i >= n:
			return i - n
		return i


def bfs_example():
	"""
	https://www.youtube.com/watch?v=EoisnPvUkOA&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=12&ab_channel=WilliamFiset

	use list as queue: https://www.geeksforgeeks.org/queue-in-python/
	list.append - enqueue back of queue
	list.pop(0) - dequeue from of queue
	instead use collections.deque for faster results
	"""
	class Node():
		def __init__(self, n):
			self.n = n
			self.visited = False
			self.neighbors = []
		def __repr__(self):
			return f"Node:{self.n}"

	# build a graph
	# a -> b -> c
	a = Node('a')
	b = Node('b')
	c = Node('b')
	a.neighbors.append(b)
	b.neighbors.append(c)

	# initialize queue
	q = [] # queue
	q.append(a)
	a.visited = True
	print(f"Visited {a}")
	while len(q) != 0: # while queue not empty
		node = q.pop(0) # dequeue
		for nbr in node.neighbors:
			if nbr.visited is False:
				nbr.visited = True
				print(f"Visited {nbr}")
				q.append(nbr)	# enqueue

def main():
	# bfs_example()
	# q = SimpleQueueUsingDeque()
	# q.enqueue(10)
	# q.enqueue(20)
	# q.enqueue(30)
	# q.dequeue()
	# print(q)

	# q = SimpleQueueUsingList()
	# q.enqueue(10)
	# q.enqueue(20)
	# q.enqueue(30)
	# q.dequeue()
	# print(q)

	q = SimpleQueueUsingFixedArray(3)
	q.enqueue(10); print(q, q._front, q._back, q.size())
	q.enqueue(20); print(q, q._front, q._back, q.size())
	q.enqueue(30); print(q, q._front, q._back, q.size())
	q.enqueue(40); print(q, q._front, q._back, q.size())
	return
	print(q._front, q._back)
	q.dequeue()
	print(q._front, q._back)
	q.dequeue()
	print(q._front, q._back)
	print(q)
	print(q.size())

main()