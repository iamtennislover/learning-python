"""
https://www.notion.so/ammul/Binary-Tree-and-Binary-Search-Tree-DS-6a41bfb93bd349c7a61db606d779a366#f2b84abc0a534cd5b862dce73c526133
	clone of https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/binarysearchtree/BinarySearchTree.java
"""
import string


class _Node:
	def __init__(self, left, right, elem, display=None):
		self.data = elem
		self.left = left
		self.right = right
		self.display = display or self.data

	def __repr__(self):
		return f"({self.left.display if self.left else ''})Node:{self.display}({self.right.display if self.right else ''})"


class BinarySearchTree:
	"""
	Basic idea is that it builds a BST tree with
	all smaller nodes on left side and larger nodes on right side
	and leaf nodes as null/None
	"""
	def __init__(self, display_map={}):
		self._root = None
		self.display_map = display_map

	def contains(self, elem) -> bool:
		# if elem exists in BST, return true, else false
		return self._contains(self._root, elem)
	
	def _contains(self, node, elem):	# recursively traverse the tree
		# NOTE: node represents root here and elem is compared wrt to root
		print(f"_contains: {node} {elem}, {node.data < elem if node != None else -1}")
		
		# base case: if leaf node reached, stop
		if node == None: return False

		# if node matched, return True
		if node.data == elem:
			return True

		# if root > elem, compare to left
		# NOTE: we are not comparing with wrt elem, hence not doing elem > node.data
		if node.data > elem:
			return self._contains(node.left, elem)
		
		# if node.data < elem:
		return self._contains(node.right, elem)
		

	def add(self, elem):
		# return true if elem added to tree, else false

		# return false since elem already exists
		if self.contains(elem): return False

		# add elem
		self._root = self._add(self._root, elem)
		return True

	def _add(self, node, elem):
		"""
		node represents the root, and elem represents
		new elem being added wrt root
		NOTE: Add the new elem wrt to node, so comparison
		happens wrt to node
		"""
		print(f"_add: {node} {elem}")
		# base case: if leaf node, add elem
		if node == None:
			return _Node(None, None, elem, self.display_map.get(elem))
		
		# wrt to root, elem is smaller, so add new elem to left of node
		if node.data > elem:
			print(f"adding to left: {node.left}")
			node.left = self._add(node.left, elem)
			# else add to the right
		else:
			print(f"adding to right: {node.right}")
			node.right = self._add(node.right, elem)
		
		return node

	def remove(self, elem):
		"""remove elem from BST, same as add
		"""
		if self.contains(elem):
			self._root = self._remove(self._root, elem)
			return True
		
		return False
	
	def _remove(self, node, elem):
		"""Similar to _add, node represents the root
		and hence elem is compared wrt to node

		Only key thing here is that we need to find and replace with successor
		"""
		if node == None: return None

		# 1st find the node
		if node.data > elem:	# travese left since elem is smaller than root
			node.left = self._remove(node.left, elem)
			return node
		if node.data < elem:	# travese right since elem is larger than root
			node.right = self._remove(node.right, elem)
			return node
		
		# 2nd once node is found, we remove by finding successor depending upon cases
		assert node.data == elem
		# case1: if node is leaf is already covered in 1st line of None comparision
		# case2,3: if node has only one child
		if node.left == None:
			return node.right	# NOTE: we only need to return since removal is dealt by 1st line of None comparision
		elif node.right == None:
			# successor is left node
			return node.left
		else:
			# case4: when both children exist,
			# find smallest node on right side (or largest node on left side)
			tmp = self._find_min(node.right)
			# swap smallest node with root node
			node.data = tmp.data
			# remove the tmp node from right tree
			node.right = self._remove(node.right, tmp.data)
			return node

	def _find_min(self, node):
		# find leftmost node having smallest value from given node onwards (i.e. root of subtree)
		while node.left != None:
			node = node.left
		return node

	def traverse_recursively(self, order_type):
		"""
		NOTE: Not using iterator for simplicity, instead when this fnc is called
		we just iterate entirely through the tree
		"""
		# base case
		self._traverse_recursively(self._root, order_type)
	
	def _traverse_recursively(self, node, order_type):
		"""Node traversal always starts from root, so node represents a root
		"""
		# base case
		if node == None:
			return
		
		if order_type == "preorder":
			print(f"preorder: {node}")
		# traverse smaller nodes 1st
		self._traverse_recursively(node.left, order_type)
		if order_type == "inorder":
			print(f"inorder: {node}")
		# traverse larger nodes later
		self._traverse_recursively(node.right, order_type)
		if order_type == "postorder":
			print(f"postorder: {node}")

	def traverse_level_order(self):
		"""
		Using a list as a queue
		queue.append(elem) - add to end of the queue
		queue.pop(0) - remove from front of the queue
		"""
		# we start traversal at root
		stack = [self._root]

		# while queue isn't empty, keep traversing
		while len(stack) != 0:
			# poll() = always the front of the queue
			node = stack.pop(0)
			# if node != None:	# NOTE: Adding this approach and not 
			# checking "if node.left != None" will add additional wasteful iterations
			print("levelorder", node)
			# 1st add left side
			# if node is leaf, skip
			if node.left != None: stack.append(node.left)
			if node.right != None: stack.append(node.right)

	def traverse_iteratively_preorder(self):
		"""
		Using list for a stack:
		insert(0) - push to top
		pop(0) - remove from top
		"""
		# start from root
		stack = [self._root]
		while len(stack) != 0:
			node = stack.pop(0)
			# similar to traverse_level_order, but use stack
			print("traverse_iteratively_preorder", node)
			# NOTE: because we are using stack, we first push right into the stack
			if node.right != None: stack.insert(0, node.right)
			if node.left != None: stack.insert(0, node.left)

	def traverse_iteratively_postorder(self):
		"""similar to traverse_iteratively_preorder, but
		because we need to print a root node at the end of navigating
		both children nodes, we need 2 stacks:
		1. one stack to navigate like traverse_iteratively_preorder,
		but push left side 1st, so that during pop of stack1,
		we push the node to stack2 which allows stack2 to be only
		used for printing
		"""
		# start from root
		_stack1 = [self._root]
		_stack2 = []
		while len(_stack1) != 0:
			node = _stack1.pop(0)
			
			# NOTE: because of postorder, left is pushed first
			if node.left != None: _stack1.insert(0, node.left)
			if node.right != None: _stack1.insert(0, node.right)
			if node != None:
				_stack2.insert(0, node)
		
		print("_stack2", _stack2)
		while len(_stack2) != 0:
			node = _stack2.pop(0)
			print("traverse_iteratively_postorder", node)

	def traverse_iteratively_inorder(self):
		"""Since inorder goes left from top to bottom and
		only then prints and then traverses right

		Similar to traverse_iteratively_preorder,
		use stack, but instead of pushing both left and right right away until stack is empty:
		1. we travese all the left (dig left) and keeping pushing to stack
		2. for 
		"""
		# stack to keep track of all traversed nodes
		stack = [self._root]
		# travering node - we start at root and use this to keep track left nodes
		trav = self._root
		while len(stack) != 0:
			print("trav before", trav)
			# if root of subtree has left child, navigate until you reach leaf
			while trav != None and trav.left != None:
				# push all left nodes to stack - at the end top stack will be the bottom node
				stack.insert(0, trav.left)
				trav = trav.left
			print("trav after", trav)	# this is always going to be bottom left node

			# find bottom left child node by popping (or right child node)
			node = stack.pop(0)
			print("popped node", node)
			# and move it to right once only, and add its right child to traverse
			if node.right != None:
				stack.insert(0, node.right)
				# now that we have right, use that as traversal node
				trav = node.right
			
			# finally print
			print("traverse_iteratively_inorder", node)



def main():
	bst = BinarySearchTree()
	# print(bst.contains(10))
	# return
	bst.add(20)
	# print(bst.contains(20))
	bst.add(10)
	print("root", bst._root.left, bst._root.right, bst._root)
	print(bst.contains(10))
	print(bst.remove(10))
	print(bst.contains(10))
	bst.add(30)
	bst.add(40)
	bst.add(50)
	bst.add(20)
	bst.add(15)
	bst.add(5)
	# print(bst._root)

	# This is primarily to map to whats displayed in
	# https://www.youtube.com/watch?v=k7GkEbECZK0&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=27&ab_channel=WilliamFiset
	A_TO_L_LIST = [11,6,15,3,8,13,17,1,5,12,14,19]
	e_to_a = {}
	for i, e in enumerate(A_TO_L_LIST):
		e_to_a[e] = list(string.ascii_uppercase)[i]
	# bst = BinarySearchTree(e_to_a)
	bst = BinarySearchTree({})
	for e in A_TO_L_LIST:
		bst.add(e)
	print("****"*10)
	print(e_to_a)
	# bst.traverse_recursively("preorder")
	# print("****"*10)
	bst.traverse_recursively("inorder")
	# print("****"*10)
	# bst.traverse_recursively("postorder")
	# print("****"*10)

	# bst.traverse_level_order()
	# print("****"*10)
	# bst.traverse_iteratively_preorder()
	# print("****"*10)
	# bst.traverse_iteratively_postorder()
	print("****"*10)
	bst.traverse_iteratively_inorder()

main()