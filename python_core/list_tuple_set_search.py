import time, string

def membership_test(container):
	for i in range(len(container)):
		if 'z' in container:
			pass

char_set = set((string.ascii_letters)*500000)
char_list = list((string.ascii_letters)*500000)
char_tuple = tuple((string.ascii_letters)*500000)

start = time.perf_counter()
membership_test(container=char_tuple)
stop = time.perf_counter()
print('pefromance Tuple:', stop-start)

start = time.perf_counter()
membership_test(container=char_list)
stop = time.perf_counter()
print('pefromance list:', stop-start)

start = time.perf_counter()
membership_test(container=char_set)
stop = time.perf_counter()
print('pefromance set:', stop-start)