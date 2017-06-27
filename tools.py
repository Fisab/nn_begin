import json
import random

with open('data.json') as data_file:
	config = json.load(data_file)

def print_number(numb):
	c = 1
	for i in numb:
		if i == 0:
			print(' ', end='')
		else:
			print('o', end='')
		if c % 3 == 0:
			print()
		c += 1
	print()

def make_teach_arr(numb):
	arr = config['numbers'][numb]
	result = []
	buf = []
	del_numbs = arr.count(1)
	result.append(arr)
	# for j in range(10):
	# 	for i in range(len(arr)):
	# 		if arr[i] == 1:
	# 			del_this_bool = bool(random.getrandbits(1))
	# 			if del_this_bool == True and del_numbs > 0:
	# 				buf.append(0)
	# 				del_numbs -= 1
	# 			else:
	# 				buf.append(1)
	# 		else:
	# 			buf.append(arr[i])
	# 	result.append(buf)
	# 	buf = []

	print(numb, len(result))
	return result

def all_numbs():
	t = config['for_learn']
	for i in t.keys():
		t[i] = make_teach_arr(i)
	with open('data1.json', 'w') as outfile:
		json.dump(config, outfile)

def all_numbs_set_null():
	t = config['weights']
	for i in t.keys():
		t[i] = [0 for i in range(15)]
	with open('data1.json', 'w') as outfile:
		json.dump(config, outfile)
#make_teach_arr('two')

if __name__ == '__main__':
	all_numbs_set_null()
	all_numbs()

#print_number([1,1,1,1,0,0,1,1,1,0,0,1,1,1,1])