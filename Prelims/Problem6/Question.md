# To The Moon!

## Problem Statement: <br>
X Æ A-12 took his friends to a birthday party or mars! They spot an alien with a very big head and no nose. He gives them a matrix of nxm blocks and goes away. Now, X Æ A-12, being the smartest person there, challenges his friends. He asks them to make a code, which will take the first row and last row, and interchange it, something like this

## Input Format: <br>
```
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
    ]
```

## Output Format: <br>
```
ans = [
    [4, 5, 6, 7],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [1, 2, 3, 4]
    ]
```


## Sample Input: <br>
```
4 7 9 1 5
3 4 7 2 6
9 9 9 9 7
8 7 6 2 8

```

## Sample Output: <br>
```
8 7 6 2 8
3 4 7 2 6
9 9 9 9 7
4 7 9 1 5
```

## Explanation:
You will be getting a list n which contains N arrays. Find the length of N. Then tak the first and last arrays and replace them.

## Constraints
The Output format should be in the same way as the input format, which is N number of subarrays inside the list mat, and each array containing M number of elements. Also, remember NOT TO CHANGE the values of the elements in each subarray. Best not to mess with them...
