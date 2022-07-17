class DynamicArray():
	def __init__(self, capacity: int):
		if capacity < 0: raise ValueError()
		self.len = 0 # user length array - initialized to 0
		self._capacity = capacity # actual array size
		self._arr = [None]*capacity # internal fixed array
		self._iter_index = 0
	
	def size(self) -> int: # O(1)
		return self.len
	
	def is_empty(self) -> bool: # O(1)
		return self.size() == 0
	
	def get(self, index: int): # access - O(1)
		if index >= self.len or index < 0: # input validation
			raise IndexError()

		return self._arr[index]
	
	def set(self, index: int, elem): # insert - O(1)
		if index >= self.len or index < 0: raise IndexError()
		self._arr[index] = elem

	def clear(self): # O(n)
		for i in range(self._capacity):
			self._arr[i] = None
		self.len = 0

	def add(self, elem): # append - O(1)
		"""Append elem to array
		NOTE: since originally self.len == 0,
		elems are added from 1st index onwards

		Logic:
		1. if new elem is going to exceed array's size
			a. create new array with double current size
			b. copy data from old array to new array
			c. use new array
		2. add the elem to the array and increment len
		"""
		# current len + elem will require a new array
		if (self.len+1 >= self._capacity):
			if self._capacity == 0:
				self._capacity = 1
			else:
				self._capacity = self._capacity * 2 # double size
			new_arr = [None]*self._capacity
			# copy
			for i in range(self.len):
				new_arr[i] = self._arr[i]
			self._arr = new_arr
    
		self._arr[self.len] = elem
		self.len = self.len + 1	# NOTE: only after assigning variable above, increase length size

	def remove_at(self, index): # O(n)
		"""Remove an elem at given index

		Logic:
		1. create new array with current capacity - 1
		2. 
		"""
		if index >= self.len or index < 0: raise IndexError()
		new_arr = [None]*(self._capacity - 1)
		j = 0	# to access new_arr
		d = self._arr[index]
		for i in range(self._capacity):	# copy
			if i == index:
				j = j - 1	# go back behind
			else:
				new_arr[j] = self._arr[i]
			j = j + 1
		self._arr = new_arr
		self.len = self.len - 1
		self._capacity = self._capacity - 1
		return d

	def index_of(self, elem): # search - O(n)
		"""get index of elem"""
		for i in range(self._capacity):
			if elem == self._arr[i]:
				return i
		return -1

	def __iter__(self):
		return self

	def __next__(self):
		if self._iter_index >= self.len:
			raise StopIteration
		r = self._arr[self._iter_index]
		self._iter_index = self._iter_index + 1
		return r

def main():
  c = 3
  d = DynamicArray(c)
  print(d.len)
  assert d.len == 0
  d.add(10)
  assert d.get(0) == 10
  for i in range(2, 4):
	  d.add(i*10)
  assert d.get(1) == 20
  assert d.get(2) == 30
  assert d.len == 3
  assert d._capacity == 6
  assert d.index_of(30) == 2

  # test iteration
  for i in d:
	  print(i)

  print(d._arr)
  assert d.remove_at(1) == 20
  assert d.get(0) == 10
  assert d.get(1) == 30
  print(d._arr)

main()
