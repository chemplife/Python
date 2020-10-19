from collections import namedtuple, defaultdict
from datetime import datetime
from functools import partial

file_name = 'project_3_data_file/nyc_parking_tickets_extract.csv'

with open(file_name) as f:
	column_headers = next(f).strip('\n').split(',')

	# Replace spaces with '_' and make everything Lowercase
	column_names = [headers.replace(' ', '_').lower() for headers in column_headers]

Ticket = namedtuple('Ticket', column_names)

# Generator Function to Read data from the file, 1 row at a time..
def read_data():
	with open(file_name) as f:
		next(f)
		yield from f

raw_data = read_data()

# Data Cleanup for 'Int' datatypes..
def parse_int(value, *, default=None):
	try:
		return int(value)
	except ValueError:
		return default

# Data Cleanup for 'DateTime' datatypes..
def parse_date(value, *, default=None):
	date_format = '%m/%d/%Y'
	try:
		return datetime.strptime(value, date_format).date()
	except ValueError:
		return default

# Data Cleanup for 'String' datatypes..
def parse_string(value, *, default=None):
	try:
		# clean empty spaces
		cleaned = value.strip()
		if not cleaned:
			return default
		else:
			return cleaned
	except ValueError:
		return default

# Tuple to format each column data with correct Datatype..
# **** Element 2 and 3 are 2 ways for doing the same thing..
column_parsers = (parse_int,
				 parse_string,
				 lambda x: parse_string(x, default=""),
				 partial(parse_string, default=""),
				 parse_date,
				 parse_int,
				 partial(parse_string, default=""),
				 parse_string,
				 lambda x: parse_string(x, default="")
				)

# Mapping the Datatype into each field..
def parse_row(row, *, default=None):
	# all the column headers
	fields = row.strip('\n').split(',')
	# Has to be a list comprehension because 'all' will go over every element and will exhaust the 'Generator Expression'..
	parsed_data = [func(field) for func, field in zip(column_parsers, fields)]

	# Check if every item in 'parsed_data' is not 'None'.. If any of the field is 'None', we drop the row..
	if all(item is not None for item in parsed_data):
		return Ticket(*parsed_data)
	return default

# Filter the returned data from 'parse_row'.. if it is None, don;t 'yield' it..
def parsed_data():
	for row in read_data():
		parsed = parse_row(row)
		if parsed :
			yield parsed

# Calculating the Number of Violations by Car-Make
def violation_count_by_make():
	makes_counts = defaultdict(int)

	for data in parsed_data():
		makes_counts[data.vehicle_make] += 1

	return {make:cnt for make, cnt in sorted(makes_counts.items(), key=lambda x: x[1], reverse=True)}

print(violation_count_by_make())