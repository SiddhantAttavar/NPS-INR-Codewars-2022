def max_profit(arr):
    price=0
    m=max(arr)
    s=0
    j=0
    for i in range(len(arr)):
        s=s+arr[i]
        if arr[i]==m:
            price=price+((j+1)*m-s)
            s=0
            j=0
            if i!=len(arr)-1:
                m=max(arr[i+1:])
        else:
            j+=1

    return price
            

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(int(max_profit(arr)))
