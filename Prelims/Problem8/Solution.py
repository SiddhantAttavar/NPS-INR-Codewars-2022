n, m = map(int, input().split())
a = [-1] * n
e = [list(map(int, input().split())) for _ in range(m)]

def get(x):
	if a[x] < 0:
		return x
	a[x] = get(a[x])
	return a[x]

def unite(x, y):
	x = get(x)
	y = get(y)

	if x == y:
		return False
	
	if a[x] < a[y]:
		x, y = y, x
	
	a[y] += a[x]
	a[x] = y
	return True

e.sort(key = lambda x: x[2])

res = 0
for u, v, w in e:
	if unite(u - 1, v - 1):
		res += w
x = get(0)
for i in range(1, n):
	if get(i) != x:
		print(-1)
		break
else:
	print(res)
