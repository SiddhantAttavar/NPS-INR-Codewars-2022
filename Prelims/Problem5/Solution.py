n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key = lambda x: x[1])

c = 0
res = 0
for i in a:
	if c < i[0]:
		res += 1
		c = i[1]

print(res)
