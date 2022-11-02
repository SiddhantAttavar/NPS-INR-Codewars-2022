from random import randint

def generate(subtask):
	# Print N
	if subtask == 1:
		n = randint(1, int(1e5))
	else:
		n = randint(1, 15)
	print(n)

	for i in range(n):
		# Print A and B
		s = randint(1, int(1e9) - 1)
		print(s, end = ' ')
		if subtask == 2:
			print(s)
		else:
			print(randint(s, int(1e9)))

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
