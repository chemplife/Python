import sys
import importer

# import module1 using our own importer.
# This should load our module1_source, create a module (module1), and put it into sys cache (sys.modules[])
module1 = importer.import_('module1', 'module1_source.py', '.')

# But after the import, module is not in the global namespace yet.
print('Module1 in global namespace?: ',module1 in globals())

# Check if sys finds the module in its modules[] directory.
# Because of mod.__file__, sys knows where module1_source came from
print('SYS says:', sys.modules.get('module1', 'module1 not found'))

# Now, module2.py can find module1
import module2

print('Module2 in global namespace?: ',module2 in globals())

# It did not find module2 in the namespace either, but since it is in the same directory as this file,
# Finder 'PathFinder' finds it in the project directory and tells the compiler to load it.
# So, it will run it.
module2.hello()

# For instance, this won't work
# importlib does what our importer.py do, just with more added things.
# So, use importlib when we want to import module through code and don't want to use regular 'import'.
math2 = 'math'
import importlib
importlib.import_module(math2)

print('Math in sys modules?: ', math2 in sys.modules)

print('Math in global namespace?: ','math' in globals())

#This will throw error
#print(math.sqrt(2))

# to add math in globals()
# way 1. math_mod = sys.modules[math2]
# way 2. math_mod = importlib.import_module(math2)
# way 3. import math as math_mod

math_mod = sys.modules[math2]

print('Math_mod in global namespace?: ','math_mod' in globals())
print('Math_mod:',math_mod.sqrt(2))