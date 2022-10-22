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

for _ in range(int(input())):
    mat = input()
    


    
