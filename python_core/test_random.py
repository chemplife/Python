import random
# Seed if constant, will create the same sequence of random number.
# Good for testing and debugging.

random.seed(0)

for _ in range(10):
	# Randint(a,b) generate random integers b/w 'a' and 'b' including 'a' & 'b'
	print(random.randint(10,20), random.random())

# Seed is used by every random_function
def generate_random_stuff(seed=None):
	random.seed(seed)

	result = []

	for _ in range(5):
		result.append(random.randint(0,5))

	character = list('abc')
	random.shuffle(character)
	result.append(character)

	for _ in range(5):
		result.append(random.gauss(0,1))

	return result

def frequency_analysis(lst):
	return {k: lst.count(k) for k in set(lst)}

lst = [random.randint(0,10) for _ in range(100)]
