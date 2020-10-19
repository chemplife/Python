def countdown(num):
	def inner():
		nonlocal num
		num -= num
		return num
	return inner

cnt = countdown(10)
cnt_iter = iter(cnt, -1)
print(help(iter))
#for num in cnt_iter:
	#print(num)