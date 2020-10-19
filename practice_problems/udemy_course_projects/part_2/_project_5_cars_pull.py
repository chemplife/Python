import csv
from itertools import islice
from collections import namedtuple


f_names = 'project_5_data_file/cars.csv', 'project_5_data_file/personal_info.csv'

# for f_name in f_names:
# 	with open(f_name) as f:
# 		print(next(f), end="")
# 		print(next(f), end="")
# 	print('\n------------------')

# As we can see both the CSV files have different flavors

# Sniffer() class has a method 'sniff'.. It reads a certain number of characters and we can determine what is the 'delimiter' in the 'file' from 'vars'
def get_dialect(f_name):
	with open(f_name) as f:
		return csv.Sniffer().sniff(f.read(1000))

# Clean the Headers and create a Namedtuple
# Then, create iterator for each row and return a Namedtuple for each row..
# Need to have a 'contextmanager' the will iterate over each row in the file
# Creating a single class for both 'contextmanager' and 'iterator'

## Using Class..
class FileParser:
	def __init__(self, f_name):
		self.f_name = f_name

	# 'Context Manager' Protocol
	def __enter__(self):
		self._f = open(self.f_name, 'r')
		self._reader = csv.reader(self._f, get_dialect(self.f_name))
		headers = map(lambda s: s.lower(), next(self._reader))
		self._nt = namedtuple('Data', headers)
		# self is returning an iterator..
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		self._f.close()
		return False

	# Iterator Protocol
	def __iter__(self):
		return self

	def __next__(self):
		if self._f.closed:
			raise StopIteration
		return self._nt(*next(self._reader))


with FileParser(f_names[1]) as data:
	for row in islice(data, 10):
		print(row)

print('\n--------------------------------------------------------------------------------')
## Using Generator Function

# iterator using Generator Function
def parsed_data_iter(data_iter, nt):
	for row in data_iter:
		yield nt(*row)


# ContextManager using Generator Function
from contextlib import contextmanager

@contextmanager
def parsed_data(f_name):
	f = open(f_name, 'r')
	try:
		reader = csv.reader(f, get_dialect(f_name))
		headers = map(lambda s: s.lower(), next(reader))
		nt = namedtuple('Data', headers)
		yield parsed_data_iter(reader, nt)
	finally:
		f.close()

with parsed_data(f_names[0]) as data:
	for row in islice(row, 5):
		print(row)