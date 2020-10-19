from collections import namedtuple

s= "I'm writing a script"

iter_s = iter(s)
#Iterator object
print(iter_s)
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))

###############################################################################

#Read whole file 
# with open('test_files/cars.csv') as file:
# 	for line in file:
		# print(line)

###############################################################################

#Read file and make a list of each row
# with open('test_files/cars.csv') as file:
# 	row_index = 0
# 	for line in file:
# 		if row_index == 0:
# 			# header row
# 			print('Headers:', line.strip('\n').split(';'))
# 		elif row_index == 1:
# 			# datatype row
# 			print('Data Types:',line.strip('\n').split(';'))
# 		else:
# 			# data rows
# 			print(f'Data Row {row_index-1}:',line.strip('\n').split(';'))
# 		row_index+=1

###############################################################################

'''
To make each data element of the datatype mentioned in the 2nd row of the file:
	- pass each element to a function to change it agains the datatype row.

* Namedtuple: to look up data using the headers from the file.
'''

def cast(data_type, data_object):
	if data_type == 'DOUBLE':
		return float(data_object )
	elif data_type == 'INT':
		return int(data_object)
	else:
		return str(data_object)

def data_cast (datatype, data):
	return [cast(datatype, value) for datatype, value in zip(datatype, data)]

# make a  car namedtuple
# The Long way to do it.
cars = []
with open('test_files/cars.csv') as file:
	row_index = 0
	for line in file:
		if row_index == 0:
			headers = line.strip('\n').split(';')
			Car = namedtuple('Car', headers)
		elif row_index == 1:
			datatypes = line.strip('\n').split(';')
		else:
			data = line.strip('\n').split(';')
			data = data_cast(datatypes,data)
			cars.append(Car(*data))
		row_index+=1
# print(f'NamedTuple data: {cars}')


# The Pythonic way of doing it
# File is iterable. So, we can get the iterator of this iterable and call next() to go to next row.
# Also, iterators get consumed as we use it. It cannot run backwards
cars = []

with open('test_files/cars.csv') as file:
	file_iter = iter(file)
	headers = next(file_iter).strip('\n').split(';')
	Car = namedtuple('Car', headers)
	datatypes = next(file_iter).strip('\n').split(';')

	# loop throught th erest of the file.
	# 1 way to do it.
	# for line in file_iter:
	# 	data = line.strip('\n').split(';')
	# 	data = data_cast(datatypes, data)
	# 	cars.append(Car(*data))

	# 2nd way of doing it.
	# Easy to understand
	# car = [data_cast(datatypes, line.strip('\n').split(';'))
	# 		for line in file_iter
	# 		]
	# cars_2 = [Car(*car_data) for car_data in car]

	# 3rd way of doing it.
	# Too turse
	cars_3 = [Car(*data_cast(
							datatypes, line.strip('\n').split(';')
							)
				)
			for line in file_iter
			]
#print(f'Cars: NamedTuple data: {cars}')
#print(f'Cars_2: NamedTuple data: {cars_2}')
#print(f'Cars_3: NamedTuple data: {cars_3}')

######################################################################
'''
Print distinct origins from the cars file.
Way 1: Read the whole file and get the info
		-> Need the big enough memory to load the entire file.
		-> Not the smartest way of doing it.

Way 2: Read 1 row at a time and get info
		-> Need big enough memory to load 1 row.
		-> Better idea	
'''
######################################################################

# Way 1

origins = set()

with open('test_files/cars.csv') as file:
	rows = file.readlines()
	for row in rows[2:]:
		origins.add(row.strip('\n').split(';')[-1])
print('Distinct Origins (Reading whole file):', origins)

# Way 2

origins = set()

with open('test_files/cars.csv') as file:
	next(file), next(file)
	for row in file:
		origins.add(row.strip('\n').split(';')[-1])
print('Distinct Origins (Reading 1 row at a time):', origins)