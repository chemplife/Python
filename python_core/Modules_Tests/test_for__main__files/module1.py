"""
To get arguments while running from commandline directly.
"""
import argparse

print(f'Name of the module file is: {__name__}')

if __name__ == '__main__':
	print("The module was run directly.\nI'm going to do some specific stuff in this case.")

	# This is how to print properties of the file, like __doc__, __file__, __name__ etc.
	parser = argparse.ArgumentParser(description=__doc__)

	# This is how to take a POSITIONAL argument in the commandline. (argument_name, type, helper_string)
	parser.add_argument('message', type=str, help="Type the message you want to print")

	# This is how to take a KEYWORD argument in the commandline. (argument_name, extended_name, type, helper_string)
	parser.add_argument('-dob', '--date_of_birth', type=int, default=1, help="Only the date of birth.")

	# Get the arguments
	args = parser.parse_args()

	print(f'Message: {args.message}')
	print(f'Dob: {args.date_of_birth}')

elif __name__ == 'module1':
	print("The module was run via import.\nI'm going to do some other stuff in this case.")