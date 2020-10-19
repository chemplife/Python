# Print pair with sum closest to the target value.
# Pick 1 element from each list.

l1 = [-1, 3, 8, 2, 9, 5]
l2 = [4, 1, 2, 10, 5, 20]
targ = 24

# Brute Force
l = []
for x1 in l1:
	for x2 in l2:
		l.append([x1, x2, abs(x1+x2-24)])
closest = sorted(l, key=lambda x: x[2])
print(tuple(closest[0][:len(closest[0])-1]))


# Optimized
lx = sorted(l1)
ly = sorted(l2)
i = 0
j = len(ly)-1
smallest_diff = abs(lx[0]+ly[0]-targ)
closest = (lx[0], ly[0])

while i < len(ly) and j>=0:
	valx = lx[j]
	valy = ly[i]
	diff = valy + valx - targ
	if abs(diff) <= smallest_diff:
		smallest_diff = abs(diff)
		closest = (valx, valy)
	if diff == 0:
		print(closest)
	elif diff < 0:
		i += 1
	else:
		j -= 1
print(closest)