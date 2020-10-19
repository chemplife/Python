import sys
print('=================================================\n\n')

print('---- Running Main.py.. Module name {0} ----'.format(__name__))

import module1

print('Main.globals: ',module1.pprint_dict('main.globals()', globals()))

# Python compiler looks for the imports in this sys.path
print('System_paths:\n',sys.path)
print('Where is module1:',sys.modules['module1'])

print('\n\n=================================================')

print('\n\n********************** Delete a Module *************************')
del globals()['module1']
