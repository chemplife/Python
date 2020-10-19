print('-------------------- Running {0} --------------------'.format(__name__))

def pprint_dict(header, dic):
	print('\n\n----------------------------------------------------------')
	print('***************** {0} *****************'.format(header))
	for key, val in dic.items():
		print(f'{key}: {val}')
	print('----------------------------------------------------------\n\n')

pprint_dict('module1.globals:', globals())
print('------------------- End Module {0} -------------------'.format(__name__))