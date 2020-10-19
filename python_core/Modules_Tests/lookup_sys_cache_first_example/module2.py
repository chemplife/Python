print('Running module2.py')

# shoudl find module1 because it is loaded to sys from our importer.py
import module1

def hello():
	print('Module2 says Hello!')
	module1.hello()