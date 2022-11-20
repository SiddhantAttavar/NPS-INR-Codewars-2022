from random import randint

def generate(subtask):
	# Print N
	n = randint(1, int(1e5))
	print(n)

	for i in range(n):
		# Print A and B
		print(randint(-int(1e9), int(1e9)), end = ' ')
		print(randint(-int(1e9), int(1e9)))

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
