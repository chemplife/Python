import constants
# import csv
import parse_utils

from itertools import islice, groupby, tee
from datetime import datetime
from functools import partial

# See a sample of what is there in each file
# for fname in constants.fnames:
# 	print(fname)
# 	with open(fname) as f:
# 		print(next(f), end='')
# 		print(next(f), end='')
# 		print(next(f), end='')
# 	print()

# using CSV
# for fname in constants.fnames:
# 	print(fname)
# 	with open(fname) as f:
# 		reader = csv.reader(f, delimiter=',', quotechar='"')
# 		print(next(reader))
# 		print(next(reader))
# 	print()

# using parse_utils file: get the headers
# for fname in constants.fnames:
# 	print(fname)
# 	reader = parse_utils.csv_parser(fname, include_header=True)
# 	print(next(reader))
# 	print()

# # using parse_utils file: get the just the Data
# for fname in constants.fnames:
# 	print(fname)
# 	reader = parse_utils.csv_parser(fname)
# 	print(next(reader))
# 	print(next(reader))
# 	print()

# Date formatter
# reader = parse_utils.csv_parser(constants.fname_update_status)
# for _ in range(3):
# 	record = next(reader)
# 	record = [str(record[0]), parse_utils.parse_date(record[1]), parse_utils.parse_date(record[2])]
# 	print(record)

# testing iter_file func
# for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
# 	file_iter = parse_utils.iter_file(fname, class_name, parser)
# 	print(fname)
# 	for _ in range(3):
# 		print(next(file_iter))
# 	print()

# Testing iter_combined_plain_tuple func
# gen = parse_utils.iter_combined_plain_tuple(constants.fnames, constants.class_names, constants.parsers, constants.compress_fields)

# print(list(next(gen)))
# print()
# print(list(next(gen)))

# Testing create_combo_named_tuple_class func
# print(list(parse_utils.create_combo_named_tuple_class(constants.fnames, constants.compress_fields)))
# nt = parse_utils.create_combo_named_tuple_class(constants.fnames, constants.compress_fields)
# print(nt._fields)

# Testing iter_combined func
# data_iter = parse_utils.iter_combined(constants.fnames, constants.class_names, constants.parsers, constants.compress_fields)

# for row in islice(data_iter, 5):
# 	print(row)
# 	print()

# print('---------------------------------------------')

# Testing filtered_iter_combined func
cutoff_date = datetime(2017, 3, 1)

# We need a grouping key for grouping data based on Gender and Vehicle_Make
def group_key(item):
	return item.gender, item.vehicle_make

data = parse_utils.filtered_iter_combined(constants.fnames, constants.class_names, constants.parsers, constants.compress_fields,
													key=lambda row: row.last_updated >= cutoff_date)


###############
#### WAY 1 ####
###############

# While grouping, we need to sort the data first, otherwise we will end up with many groups with same 'Key'
sorted_data = sorted(data, key=group_key)

# Creating Groups
groups = groupby(sorted_data, key=group_key)

# filter groups by 'gender'
# This will create a 'Shallow Copy' of groups in 2 variables.. It is not making copy of the 'subiterators' inside these new groups..
# group_1, group_2 = tee(groups)
# So, we will just do what we did in line '92'

groups_1 = groupby(sorted_data, key=group_key)
groups_2 = groupby(sorted_data, key=group_key)

group_f = (item for item in groups_1 if item[0]=='Female')
# To Just get the vehicle_make and the number of times they occur in the 'group'
data_f = ((item[0][1], len(list(item[1]))) for item in group_f)

group_m = (item for item in groups_2 if item[0]=='Male')
data_m = ((item[0][1], len(list(item[1]))) for item in group_m)


###############
#### WAY 2 ####
###############
# Create Groups for 'Male' and 'Female' directly..

# Since 'data' contains Tuples, it is ok to do 'Shallow Copy'
data_1, data_2 = tee(data, 2)

data_m = (row for row in data_1 if row.gender == 'Male')
data_f = (row for row in data_2 if row.gender == 'Female')

# We don't need 'Gender' in our grouping key now..
# We need a grouping key for grouping data based on Gender and Vehicle_Make
def group_key(item):
	return item.vehicle_make

sorted_data_m = sorted(data_m, key=group_key)
groups_m = groupby(sorted_data_m, key=group_key)
group_m_counts = ((g[0], len(list(g[1]))) for g in groups_m)

sorted_data_f = sorted(data_f, key=group_key)
groups_f = groupby(sorted_data_f, key=group_key)
group_f_counts = ((g[0], len(list(g[1]))) for g in groups_f)


###############
#### WAY 3 ####
###############
# Do 'Way 2' with a 'function'
# Check 'parse_utils' for that.. 'group_data' func

def filter_key(cutoff_date, gender, row):
	return row.last_updated >= cutoff_date and row.gender == gender


results_f = parse_utils.group_data(constants.fnames, constants.class_names, constants.parsers, constants.compress_fields,
									filter_key=partial(filter_key, cutoff_date, 'Female'), group_key=lambda row: row.vehicle_make)

results_m = parse_utils.group_data(constants.fnames, constants.class_names, constants.parsers, constants.compress_fields,
									filter_key=lambda row: filter_key(cutoff_date, 'Male', row), group_key=lambda row: row.vehicle_make)

for row in results_f:
	print(row)
print()
for row in results_m:
	print(row)