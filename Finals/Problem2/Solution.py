# Loop through all testcases
for _ in range(int(input())):
	# Take input and print sum
	n, k = map(int, input().split())
	s = input()

	r = s.count('R')
	g = s.count('G')

	if r != g:
		print('NO')
		continue

	if k == int(1e9):
		print('YES')
		continue

	a = 0
	b = 0
	for i in range(n - 1):
		if s[i] == s[i + 1]:
			if s[i] == 'R':
				a += 1
			else:
				b += 1
	
	if a == 1 and b == 1:
		print('YES')
	else:
		print('NO')
