n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp1 = [0] * n
dp2 = [0] * n

dp1[0] = a[0]
dp2[0] = b[0]

for i in range(1, n):
	dp1[i] = max(dp1[i - 1], dp2[i - 1] + a[i])
	dp2[i] = max(dp2[i - 1], dp1[i - 1] + b[i])

print(max(dp1[n - 1], dp2[n - 1]))	
