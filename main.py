import json
import tools

class Neuron():
	def __init__(self):
		self.weights = {}
		self.entry = 7
		self.decides = {}
		self.load_data()
	###
	def load_config(self):
		with open('data1.json') as data_file:
			config = json.load(data_file)
		return config

	def load_data(self):
		config = self.load_config()
		keys = config['weights'].keys()
		for i in keys:
			self.decides[i] = 0
			self.weights[i] = config['weights'][i]
	###
	def get_weights(self, key):
		return self.weights[key]

	def load_weights(self, arr, key):
		self.weights[key] = arr

	def get_all_weights(self):
		return self.weights
	###
	def sum(self, arr, key):
		res = 0
		for i in range(len(arr)):
			res += arr[i] * self.weights[key][i]
		return res

	def activation(self, res, key):
		self.decides[key] = res >= self.entry

	def think(self, numb, key):
		summ = self.sum(numb, key)
		result = self.activation(summ, key)

	def main(self, numb):
		for i in self.weights.keys():
			self.think(numb, i)

		return self.decides

def print_true(arr):
	know = False
	for i in arr.keys():
		if bool(arr[i]) == True:
			print(i, arr[i])
			know = True
	if know == False:
		print('I don`t know what is this :(')

def test(numb):
	if type(numb) == type(''):
		with open('data.json') as data_file:
			config = json.load(data_file)
		arr = config['numbers'][numb]
	else:
		arr = numb
	n = Neuron()
	a = n.main(arr)
	print_true(a)

if __name__ == '__main__':
	test('one')
	test('two')
	test('three')
	test('four')
	test('five')
	test('six')
	test('seven')
	test('eight')
	test('nine')
	test('zero')