class BinarySearchTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, data):
		if data == self.data:
			return

		if data < self.data:
			# add data in left sub-tree
			# check if left-subtree has data
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinarySearchTree(data)

		else:
			# add data in right sub-tree
			# check if left-subtree has data
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinarySearchTree(data)

	# Do In-Order-Traversal: List will be in Ascending Order
	def in_order_traversal(self):
		element = []
		# Visit left-tree, then visit base-node, then visit right-tree
		if self.left:
			element += self.left.in_order_traversal()
		element.append(self.data)
		if self.right:
			element += self.right.in_order_traversal()
		return element

	def search(self, val):
		if self.data == val:
			return True

		if val < self.data:
			# look in left
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			# look in right
			if self.right:
				return self.right.search(val)
			else:
				return False

	def find_min(self):
		if self.left:
			return self.left.find_min()
		return self.data

	def find_max(self):
		if self.right:
			return self.right.find_max()
		return self.data

	def delete_val(self, val):
		# way 1: find min from right-tree and copy that value to the node of 'val' and remove duplicate
		# way 2: find max from left-tree and copy that value to the node of 'val' and remove duplicate
		# Find val first:
		if self.data > val:
			if self.left:
				self.left = self.left.delete_val(val)
		elif self.data < val:
			if self.right:
				self.right = self.right.delete_val(val)
		# Found match.
		else:
			if self.left is None and self.right is None:
				# No Need to find replacement
				return None
			elif self.right is None:
				# Find max in Left Tree
				replace_val = self.left.find_max()
				self.left = self.left.delete_val(replace_val)
			else:
				# Find Min in Right Tree
				replace_val = self.right.find_min()
				self.right = self.right.delete_val(replace_val)
			
			self.data = replace_val

		return self

	def insert_val(self, val):
		pass


def build_tree(lst):
	root = BinarySearchTree(lst[0])
	for i in range(1, len(lst)):
		root.add_child(lst[i])

	return root


if __name__ == '__main__':
	numbers = [17, 4, 1, 21, 9, 25, 19, 34, 18, 22, 23, 24, 31, 37]
	binary_tree = build_tree(numbers)
	print(binary_tree.in_order_traversal())
	print(binary_tree.search(21))
	print(binary_tree.find_min())
	print(binary_tree.delete_val(21))
	print(binary_tree.in_order_traversal())
	print(binary_tree.delete_val(25))
	print(binary_tree.in_order_traversal())
	print(binary_tree.delete_val(9))
	print(binary_tree.in_order_traversal())