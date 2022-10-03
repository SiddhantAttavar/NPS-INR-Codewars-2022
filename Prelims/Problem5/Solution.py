def max_profit(arr):
    m = arr.pop()
    maxsum = 0
    arrsum = 0
    for p in reversed(arr):
        m = max(m, p)
        maxsum += m
        arrsum += p
    return maxsum - arrsum

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(int(max_profit(arr)))
