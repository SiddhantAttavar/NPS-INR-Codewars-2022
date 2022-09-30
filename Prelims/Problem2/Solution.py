def binary_number(arr):
    count = 0
    arr2 = arr[::-1]
    for i in range(len(arr)):
        count = count + (2**i)*arr2[i]
    return count

