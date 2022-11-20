from random import randint

def generate(subtask):
	# Print N
	if subtask == 1:
		n = randint(1, 15)
	else:
		n = randint(1, int(1e5))
	print(n)

	for i in range(n):
		# Print A
		print(randint(0, int(1e9)), end = ' ')
	print()

	for i in range(n):
		# Print B
		print(randint(0, int(1e9)), end = ' ')

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
