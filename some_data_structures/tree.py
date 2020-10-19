class Tree:
	def __init__(self, data):
		self.data = data
		self.child = []
		self.parent = None

	def add_child(self, child):
		if isinstance(child, Tree):
			child.parent = self
			self.child.append(child)
		else:
			raise TypeError('Child is not of Tree-Type')

	# Count number of ancestors
	def get_level(self):
		level = 0
		ans = self.parent
		while ans:
			ans = ans.parent
			level += 1
		return level

	def print_tree(self):
		spaces = ' ' * self.get_level() * 3
		prefix = spaces + '|-- ' if self.parent else ""
		print(prefix + self.data)
		if self.child:
			for child in self.child:
				child.print_tree()

def build_product_tree():
	root = Tree('Electronics')

	laptop = Tree('Laptops')
	laptop.add_child(Tree('Mac'))
	laptop.add_child(Tree('Serface'))
	laptop.add_child(Tree('Thinkpad'))

	cellphone = Tree('Cellphones')
	cellphone.add_child(Tree('iPhone'))
	cellphone.add_child(Tree('Android'))
	cellphone.add_child(Tree('Windows Phone'))

	tv = Tree('Television')
	tv.add_child(Tree('Sony'))
	tv.add_child(Tree('Samsung'))
	tv.add_child(Tree('LG'))

	root.add_child(laptop)
	root.add_child(cellphone)
	root.add_child(tv)

	return root

if __name__ == '__main__':
	root = build_product_tree()
	root.print_tree()