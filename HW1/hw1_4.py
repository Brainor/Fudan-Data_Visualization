import numpy as np
import copy

def nlargest(array, n):
	'''
	We will use selection sort algorithm.
	'''
	length = len(array)
	if n > length or n < 0:
		raise Exception("Error!")

	new_array = copy.deepcopy(array)
	for i in range(length):
		for j in range(i+1,length):
			if new_array[j] > new_array[i]:
				new_array[j], new_array[i] = new_array[i], new_array[j]
		if i == n-1:
			result = new_array[i]
			break

	return result

test_data = np.random.randint(1,100,10)
print(test_data)
answer = nlargest(test_data, 3)
print(answer)

