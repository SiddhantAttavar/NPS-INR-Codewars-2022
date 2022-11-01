def Replace(mat):
    n = len(mat)
    for i in range(n-1):
        x = mat[0]
        mat.pop(0)
        mat.append(x)
    y = mat[1]
    mat.pop(1)
    mat.append(y)
    return mat

n = int(input("Please enter number of rows"))
m = int(input("Please enter number of coloumns"))
mat = []
for k in range(m):
    temp = []
    for l in range(n):
        a = int(input())
        temp.append(a)
    mat.append(temp)
    


    
