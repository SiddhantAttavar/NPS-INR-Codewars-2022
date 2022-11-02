from random import randint

def generate(subtask):
	# Print N
	if subtask == 1:
		n = randint(1, 15)
	elif subtask == 2:
		n = randint(1, 100)
	else:
		n = randint(1, int(1e5))
	m = randint(1, min(int(1e5), n * (n + 1) // 2))
	print(n, m)

	for i in range(m):
		# Print A and B
		print(randint(1, n), end = ' ')
		print(randint(1, n), end = ' ')
		print(randint(0, int(1e9)))

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
