'''
Given a staircase of 'N' steps.
We can take {1,2} steps or {1,3,5} steps at a time [{1,2} and {1,3,5} are 2 variations of this problem]
-> a set of No. of steps allowed will be give.

Write a function that will take 'N' and the 'Steps-Set' and return the 'No. of possible ways' in which we can climb the stairs
'''
'''
My Solution:
n = 4, step = 1, allowed_step={1,3}
def exact_sum(n, step, allowed_steps, current_sum=[]):
	current_sum.append(step)	# [1]
	for s in allowed_steps:
		if (sum(current_sum) + s) < n:
			return exact_sum(n, step, allowed_steps, current_sum= current_sum)
		elif (sum(current_sum) + s) == n:
			return current_sum.append(s)
		else:
			return None

def num_ways(n, steps):
	allowed_steps = {step for step in steps if step < n}
	# allowed_steps. = {1,3}

	# Sum of exact 4 out of the elements in 'allowed_steps'
	# Output is the list of lists that will hold the exact steps taken
	output = []
	for step in allowed_steps:
		result = exact_sum(n, step, allowed_steps)
		if result:
			output.append(result)

	# length of 'output' will be the no. of ways to climb the stairs
	return len(output)
'''

## NOT READY..

def exact_sum(n, step, allowed_steps, current_sum):
	sequences = []
	current_sum.append(step)	# [3]
	print('current_sum:', current_sum)
	for s in allowed_steps:
		if (sum(current_sum) + s) < n:
			s_s = exact_sum(n, step, allowed_steps, current_sum)
			if isinstance(s_s, list) and len(sequences) != 0:
				sequences = s_s
			else:
				sequences.append(s_s)
		elif (sum(current_sum) + s) == n:
			return current_sum.append(s)
		else:
			return None
	return sequences

def num_ways(n, steps):
	allowed_steps = {step for step in steps if step < n}
	output = []
	for step in allowed_steps:
		result = exact_sum(n, step, allowed_steps, list())
		print('Result:', result)
		if result:
			output.append(result)
			print('Output:', output)
	return len(output)


if __name__ == '__main__':
	n = 4
	steps = {1,3,5}
	print('No. of ways to climb Stairs: ', num_ways(n, steps))