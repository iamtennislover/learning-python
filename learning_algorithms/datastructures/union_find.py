class UnionFind():

	def __init__(self, n: int):
		"""Represents a UnionFind DS
		Clone of https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/unionfind/UnionFind.java

		Builds an array of size n with elems from 0 to n-1
		Usage:
		u = UnionFind(3)
		# returns the root set elem 0 belongs to
		root = u.find(0)
		# joins two sets 1,2
		u.unify(1,2)
		"""
		# no. of elems
		self.n = n
		# an array with index as node and value as the root node
		# i.e. value = set the node belongs to
		# defaults to i == self._id[i] meaning each node is its own set
		self._id = [i for i in range(self.n)]
		# represents sizes of each set, defaults to single item set
		self._size = [1 for i in range(self.n)]

	def find(self, p: int) -> int:
		"""for a given node, find the root set it belongs to
		takes: ~O(1)
		"""
		# since a node points to a parent which can be another child,
		# find until we reach root (which would be when _id[x] == x)
		# e.g. in "Example-Graph1" of https://www.notion.so/ammul/1-Analysis-of-Algorithm-b4dfd7e7ee354435a4871355c82c01b9#581a745604fe4fcebe0a05a3cc266c0c
		# in case 0-1-2-3 are connected, we would have [0,0,0,2] and find(3) would:
		# 1st iteration: p=3; 3 != 2; root = 2;
		# 2nd iteration: root=2; 2 != 0; root = 0;
		# 3rd iteration: stop 0 == 0
		root = p
		while root != self._id[root]:
			print("modify root", p, root, self._id[root])
			root = self._id[root]
		
		# NOTE: Above will take W(n), but with below path compression
		# when get to ~O(1)
		'''e.g. in case 0-1-2-3 are connected, we would have [0,0,0,2] and find(3) would:
		1st iteration: root=0; p=3; 3!=0; next_root=2; _id[3]=0; p=2
		2nd iteration: root=0; p=2; 2!=0; next_root=0; _id[2]=0; p=0
		3rd iteration: root=0; p=0; 0==0; stop
		'''
		while p != root:
			print("path compression", p, root, self._id[p])
			next_root = self._id[p]
			self._id[p] = root
			p = next_root
		
		return root
	
	def find_recursion(self, p):
		"""Same as find, but using recursion
		"""
		root = self._id[p]
		if root == p:
			return root
		self._id[p] = self.find_recursion(root)
		return self._id[p]
	
	def connected(self, p, q):	# return true if p and q are in same set
		return self.find(p) == self.find(q)
	
	def union(self, p, q):
		"""
		unify two sets, one set containing p and other containing q
		The union on array would simply update the values of p and q
		to store the root depending upon the size of the set - in our case
		point the smaller set to the larger set

		Logic:
		1. if same set, skip
		2. update _id
		"""
		if self.connected(p, q):
			return False	# p,q already in same set
		
		rootp = self.find(p)
		rootq = self.find(q)
		# merge smaller set into larger set
		# NOTE: we are only updating the root's value as that is only required
		'''e.g.
		1. union(0,1): 0-1
		we start with _id = [0,1,2,3]
		we end with _id = [0,0,2,3]

		2. union(2,3): 2-3
		we start with _id = [0,0,2,3]
		we end with _id = [0,0,2,2]

		3. union(1,2): 0-1-2-3
		we start with _id = [0,0,2,3]
		we end with _id = [0,0,0,2]
		'''
		if self._size[rootp] < self._size[rootq]:
			print("p is smaller", p, q)
			smallroot = rootp
			bigroot = rootq
		else:
			print("q is smaller or equal", p, q)
			smallroot = rootq
			bigroot = rootp

		print("merging small into big", smallroot, bigroot)
		# pointing small root -> big root
		self._id[smallroot] = bigroot
		self._size[bigroot] += self._size[smallroot]
		self._size[smallroot] = 0


def detect_cycle():
	"""
	"1.12 Disjoint sets data structures - weighted union and collpapsing find"
	https://www.notion.so/1-Analysis-of-Algorithm-b4dfd7e7ee354435a4871355c82c01b9
	"""
	pass


def main():
	print("Running union find")
	n = 4
	s = UnionFind(n)
	# print(s._id)
	# s._id = [0,0,0,2]
	# print(s.find(3))
	# print(s.find_recursion(3))
	s.union(0,1)
	print(s._id)
	s.union(2,3)
	print(s._id)
	s.union(1,2)
	print(s._id)
	pass

main()