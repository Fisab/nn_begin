import main
import json
import random

n = main.Neuron()

# Подать на входы нейросети цифру в строковом формате.
# Если цифра распознана/отвергнута верно, то перейти к шагу 1.
# Если сеть ошиблась и распознала неверную цифру как 5, то вычесть из всех связей, связанных с возбудившимися S-элементами единицу.
# Если сеть ошиблась и отвергла цифру 5, то добавить единицу ко всем связям, связанным с возбудившимися S-элементами.


with open('data1.json') as data_file:
	config = json.load(data_file)

def modify_weights(arr1, arr2, type_):
	p = 1
	for i in range(len(arr1)):
		if arr1[i] == 1:
			if type_ == 'increase':
				arr2[i] += p
			elif type_ == 'decrease':
				arr2[i] -= p
	return arr2

def teach():
	dict_keys = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
	learn = config['for_learn']
	for i in range(100000):
		a = random.randint(0, 9)
		key = dict_keys[str(a)]
		arr = learn[key]
		ind = random.randint(0, len(arr)-1)
		r = n.main(arr[ind])

		if bool(r[key]) == False:
			weights = n.get_weights(key)
			new_weights = modify_weights(arr[ind], weights, 'increase')
			n.load_weights(new_weights, key)

		for o in r.keys():
			if o != key and bool(r[o]) == True:
				weights = n.get_weights(o)
				new_weights = modify_weights(arr[ind], weights, 'decrease')
				n.load_weights(new_weights, o)
teach()

new_weights = n.get_all_weights()
for i in new_weights.keys():
	config['weights'][i] = new_weights[i]
print(new_weights)
with open('data1.json', 'w') as outfile:
	json.dump(config, outfile)