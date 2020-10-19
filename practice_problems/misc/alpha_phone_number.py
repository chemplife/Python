'''
 ----  ----  ----
|	 |		|	 |
| 1  |	2	| 3  |
|	 |	abc	|def |
 ----  ----  ----
|	 |		|	 |
| 4  |	5	| 6	 |
|ghi |	jkl	|mno |
 ----  ----  ----
|	 |		|	 |
| 7	 |	8	| 9	 |
|pqrs|	tuv	|wxyz|
 ----  ----  ----
 	 |		|
	 |	0	|
	 |		|
 	   ----  

Eg:
	1800 356 9377	-> 1800 Flowers
	253 6368		-> clement or clemdot or

input -> Phonenumber and list of strings
phoneNum = '3662277'
words = ['foo', 'bar', 'baz', 'foobar', 'emo', 'cap', 'car', 'cat']

Words that happen to be in the phone number
Output = ['bar', 'cap', 'car', 'emo', 'foo', 'foobar']
'''
'''
My Solution:

check_func(word, phonenum):
word_dict= {
'2' = ['a', 'b', 'c'],
'3' = ['d', 'e', 'f'],
'4' = ['g', 'h', 'i'],
'5' = ['j', 'k', 'l'],
'6' = ['m', 'n', 'o'],
'7' = ['p', 'q', 'r', 's'],
'8' = ['t', 'u', 'v'],
'9' = ['w', 'x', 'y', 'z']
}

num_list = list(phonenum)
# num_list = ['3','6','6','2','2','7','7']
trans_num_list = [['d', 'e', 'f'], ['m', 'n', 'o'], ['m', 'n', 'o'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['p', 'q', 'r', 's'], ['p', 'q', 'r', 's']]
word_list = list(word)
# word_list = ['b', 'a', 'z']
count_w = 0
for w in word_list:
	count = 0
	count_w += 1	# b = 1, a = 2, z =3
	for tnl in trans_num_list:
		count += 1	# 3 => 1, 6 => 2, 6 => 3, 2 => 4
		if w in tnl:
			break
		if count == len(trans_num_list):
			return False
	if count_w == len(word_list):
		return True



return True or False

main:
check = False
output = []
phonenum = '3662277'
for word in words:
	check = check_func(word, phonenum)
	if check:
		output.append(word)

print(output)
'''

def check_func(word, phone_list):
	word_list = list(word)
	# word_list = ['b', 'a', 'z']
	if len(word_list) > len(phone_list):
		return False
	count_w = 0
	for w in word_list:
		count = 0
		count_w += 1	# b = 1, a = 2, z =3
		for tnl in phone_list:
			count += 1	# 3 => 1, 6 => 2, 6 => 3, 2 => 4
			if w in tnl:
				break
			if count == len(phone_list):
				return False
		if count_w == len(word_list):
			return True

def phone_dict(phonenum):
	word_dict= {
		'2' : ['a', 'b', 'c'],
		'3' : ['d', 'e', 'f'],
		'4' : ['g', 'h', 'i'],
		'5' : ['j', 'k', 'l'],
		'6' : ['m', 'n', 'o'],
		'7' : ['p', 'q', 'r', 's'],
		'8' : ['t', 'u', 'v'],
		'9' : ['w', 'x', 'y', 'z']
	}

	num_list = list(phonenum)
	# num_list = ['3','6','6','2','2','7','7']
	trans_num_list = []
	for key in num_list:
		trans_num_list.append(word_dict[key])
	#trans_num_list = [['d', 'e', 'f'], ['m', 'n', 'o'], ['m', 'n', 'o'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['p', 'q', 'r', 's'], ['p', 'q', 'r', 's']]
	return trans_num_list

if __name__ == '__main__':
	check = False
	output = []
	phonenum = '3662277'
	words = ['foo', 'bar', 'baz', 'foobar', 'emo', 'cap', 'car', 'cat', 'foobaremo']
	phone_list = phone_dict(phonenum)
	
	for word in words:
		check = check_func(word, phone_list)
		if check:
			output.append(word)

	print(output)
