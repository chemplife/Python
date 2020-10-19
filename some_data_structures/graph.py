from collections import defaultdict
class Graph:
	def __init__(self, edges):
		self.edges = edges
		self.graph_dict = defaultdict(list)
		for edge in edges:
			self.graph_dict[edge[0]].append(edge[1])

	def get_graph(self):
		return self.graph_dict

	def find_path(self, start, dest, path=[]):
		path = path + [start]
		paths = []
		if start == dest:
			return [path]
		for place in self.graph_dict[start]:
			if place not in path:
				# print('Path: ', path)
				new_path = self.find_path(place, dest, path)
				# print('New Path: ', new_path)
				for p in new_path:
					paths.append(p)
				# print('Place at:', place)
		return paths

	def find_shortest_path(self, start, dest):
		paths = sorted(self.find_path(start, dest), key=lambda x: len(x))
		# If want only 1, return paths[0]
		return [path for path in paths if len(path)==len(paths[0])]


if __name__ == '__main__':
	routes = [
		('Mumbai', 'Paris'),
		('Mumbai', 'Dubai'),
		('Paris', 'Dubai'),
		('Paris', 'New York'),
		('Dubai', 'New York'),
		('New York', 'Toronto')
	]

	route_graph = Graph(routes)
	print('graph:', route_graph.get_graph())
	print('Routes to New York:', route_graph.find_path('Mumbai', 'Toronto'))
	print('Shortest Routes to New York:', route_graph.find_shortest_path('Mumbai', 'New York'))