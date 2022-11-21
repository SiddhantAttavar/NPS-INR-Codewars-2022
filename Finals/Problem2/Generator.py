from random import randint

def generate(subtask):
	# Print T
	t = randint(1, 100)
	print(t)
	for _ in range(t):
		n = randint(1, int(1e3))
		if subtask == 1:
			k = int(1e9)
		else:
			k = 1
		print(n, k)

		s = ''
		for i in range(n):
			s += 'RG'[randint(0, 1)]
		print(s)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
