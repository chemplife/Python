# move 'e' in front

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print('original dict:', d)

for key in range(len(d)-1):
	key = next(iter(d.keys()))
	d[key] = d.pop(key)

print('Rotated dict:', d)