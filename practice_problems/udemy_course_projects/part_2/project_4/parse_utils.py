import csv
from datetime import datetime
from collections import namedtuple
from itertools import chain, compress, groupby


# give out row-by-row data from the passed file.
def csv_parser(fname, *, delimiter=',', quotechar='"', include_header=False):
	with open(fname) as f:
		# if we don't want the 1st header row..
		if not include_header:
			next(f)
		reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
		yield from reader


# datetime formatter
def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
	return datetime.strptime(value, fmt)


# To get list of headers
def extract_field_names(fname):
	reader = csv_parser(fname, include_header=True)
	return next(reader)


# Creating Namedtuples for each file
def create_named_tuple_class(fname, class_name):
	fields = extract_field_names(fname)
	return namedtuple(class_name, fields)


# Creating field names for combined file
def create_combo_named_tuple_class(fnames, compress_fields):
	# We will be using only once.. so 'compress_fields' can be an 'Iterator'
	compress_fields = chain.from_iterable(compress_fields)

	# creating all field_names into 1.. using comprehension
	field_names = chain.from_iterable(extract_field_names(fname) for fname in fnames)
	compressed_field_names = compress(field_names, compress_fields)
	return namedtuple('Data', compressed_field_names)


# iterating over entire file
def iter_file(fname, class_name, parser):
	nt_class = create_named_tuple_class(fname, class_name)
	reader = csv_parser(fname)
	for row in reader:
		parsed_data = (parse_fn(value) for value, parse_fn in zip(row, parser))
		yield nt_class(*parsed_data)

# Combined files
def iter_combined_plain_tuple(fnames, class_names, parsers, compress_fields):
	# We need 'Compress_fields' to be an 'Iterable'.. because we need this in 'for loop' for every data_row
	compress_fields = tuple(chain.from_iterable(compress_fields))
	zipped_tuples = zip(*(iter_file(fname, class_name, parser)
							for fname, class_name, parser
							in zip(fnames, class_names, parsers)))

	# Chain Together the 4 iterators in 'zipped_tuples'.. Here we will get 'SSNs' multiple times
	merged_iter = (chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
	
	# Applying compress_fields to get 'SSN' field 1 time..
	for row in merged_iter:
		compressed_row = compress(row, compress_fields)
		yield tuple(compressed_row)


# Creating a combined row from each file..
def iter_combined(fnames, class_names, parsers, compress_fields):
	# Creating a custom Namedtuple for our combined file..
	combo_nt = create_combo_named_tuple_class(fnames, compress_fields)

	# We need 'Compress_fields' to be an 'Iterable'.. because we need this in 'for loop' for every data_row
	compress_fields = tuple(chain.from_iterable(compress_fields))
	zipped_tuples = zip(*(iter_file(fname, class_name, parser)
							for fname, class_name, parser
							in zip(fnames, class_names, parsers)))

	# Chain Together the 4 iterators in 'zipped_tuples'.. Here we will get 'SSNs' multiple times
	merged_iter = (chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
	
	# Applying compress_fields to get 'SSN' field 1 time..
	for row in merged_iter:
		compressed_row = compress(row, compress_fields)
		# namedtuple expect a list of args.. so we have to unpack 'compressed_row' which is an 'Iterator'
		yield combo_nt(*compressed_row)


# Filtering out data with 'last_update_date' < 'key'.. 
def filtered_iter_combined(fnames, class_names, parsers, compress_fields, *, key=None):
	iter_combo  = iter_combined(fnames, class_names, parsers, compress_fields)
	yield from filter(key, iter_combo)



# 'Way 3' to create groups..
def group_data(fnames, class_names, parsers, compress_fields, filter_key, group_key, gender=None):
	data = filtered_iter_combined(fnames, class_names, parsers, compress_fields, key=filter_key)
	sorted_data = sorted(data, key=group_key)
	groups = groupby(sorted_data, key=group_key)
	group_counts = ((g[0], len(list(g[1]))) for g in groups)

	return sorted(group_counts, key=lambda row: row[1], reverse=True)
