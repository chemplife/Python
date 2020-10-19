"""
When we run a program, there is an entry point to the program and it is a module.
And that entry point module name is changed to '__main__' by the Python.
"""
print(f'Name fo the run.py file is: {__name__}')

import module1

if __name__ == '__main__':
	print(f'{__file__} is the program entry point.')