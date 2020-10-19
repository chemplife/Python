'''
Polygon:

n = No. of edges (or vertices)
R = circumradius of the circle

Interior Angle	= (n-2) * (180/n)
edge length (s)	= 2 * R * sin(pi/n)
apothem	(a)		= R * cos(pi/n)
area			= (1/2) * n * s * a
'''

'''
Unit-Test:

assert->	checks if the given expression is True or not.
Syntax-> 	assert <condition>, <Message if condition retrin False>
use->		assert 1 > 10, '1 is not greater than 10'


'''
import math

class Polygon:
	def __init__(self, n, r):
		if n < 3:
			raise ValueError('Polygon must have atleast 3 sides')
		self._num_vertices = n
		self._circumradius = r

	def __repr__(self):
		return f'This is a polygon with {self._num_vertices} edges and {self._circumradius} circumradius.'

	def __eq__(self, other):
		if isinstance(other, Polygon):
			return (self._num_vertices == other._num_vertices) and (self._circumradius == other._circumradius)
		else:
			return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Polygon):
			return (self._num_vertices > other._num_vertices)
		else:
			return NotImplemented

	@property
	def edges(self):
		return self._num_vertices

	@property
	def vertices(self):
		return self._num_vertices

	@property
	def circumradius(self):
		return self._circumradius

	@property
	def interior_angle(self):
		return (self._num_vertices - 2) * (180/self._num_vertices)

	@property
	def edge_length(self):
		return 2 * self._circumradius * math.sin(math.pi/self._circumradius)

	@property
	def apothem(self):
		return self._circumradius * math.cos(math.pi/self._num_vertices)

	@property
	def area(self):
		return 0.5 * self._num_vertices * self.apothem * self.edge_length

	@property
	def perimeter(self):
		return self._num_vertices * self.edge_length


class Polygons:
	def __init__(self, max_n, r):
		if max_n < 3:
			raise ValueError('Polygon must have atleast 3 sides')
		self.max_ver_num = max_n
		self.circumradius = r
		self.polygons = [Polygon(i, self.circumradius) for i in range(3, self.max_ver_num+1)]

	# @property
	# def max_area_perimeter_ratio(self):
	# 	ratio = [i.area/i.perimeter for i in self.polygons]
	# 	max_ratio = max(ratio)
	# 	ind = ratio.index(max_ratio)
	# 	print('Polygon with max area-perimeter ratio: ', self.polygons[ind])
	@property
	def max_area_perimeter_ratio(self):
		sorted_polygons = sorted(self.polygons, key=lambda p: p.area/p.perimeter, reverse=True)
		return sorted_polygons[0]

	def __getitem__(self, val):
		return self.polygons[val]

	def __len__(self):
		return self.max_ver_num - 2

	def __repr__(self):
		return f'Polygons(max_n = {self.max_ver_num}, circumradius = {self.circumradius})'


polygns = Polygons(8, 1)
for p in polygns:
	print(p)
print('Max Area to perimeter Ratio Polygon:',polygns.max_area_perimeter_ratio)

def test_polygon():
	rel_tol = 0.001
	abs_tol = 0.001

	try:
		p = Polygon(2, 20)
		# assert <condition>, <message to be printed when condition returns False>
		assert False, 'Creating Polygon with 2 sides. Exception excepted, but not received.'
	except ValueError:
		pass

	n = 3
	r = 1
	p = Polygon(n, r)
	assert str(p) == f'Polygon(n=3, r=1)', f'actual: {str(p)}'
	assert p.vertices == n, f'Actual Vertices count: {p.vertices}, expected: {n}'
	assert p.edges == n
	assert p.circumradius == r
	assert p.interior_angle == 60

	n = 4
	r = 1
	p = Polygon(n, r)
	assert math.isclose(p.interior_angle, 90.0, rel_tol=rel_tol, abs_tol=abs_tol)
	assert math.isclose(p.area, 2.0, rel_tol=rel_tol, abs_tol=abs_tol), f'Actual Area: {p.vertices}, expected: {2.0}'
	assert math.isclose(p.edge_length, math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)
	assert math.isclose(p.perimeter, 4*math.sqrt(2), rel_tol=rel_tol, abs_tol=abs_tol)
	assert math.isclose(p.apothem, 0.707, rel_tol=rel_tol, abs_tol=abs_tol)

	p1 = Polygon(3, 100)
	p2 = Polygon(10, 10)
	p3 = Polygon(15, 10)
	p4 = Polygon(15, 100)
	p5 = Polygon(15, 100)
	assert p2 > p1
	assert p2 < p3
	assert p3 != p4
	assert p1 != p4
	assert p4 == p5