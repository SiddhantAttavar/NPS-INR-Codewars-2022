# The Milky Way's Chamber of Secrets
## Problem Statement: <br> 
Mars is the head of a matrix of planets in the Milky Way. After Mars, many other planets were forming a triangle. It looks something like this:
```
        0
       2 4
      6 8 10
    12 14 16 18
   20 22 24 26 28
```
and so on infinitely.  

Can you make a code to sum up all the numbers in a given line _N_?

## Input format: <br>
 - A single line of input containing the integer _N_

## Output format: <br>
 - A single integer representing the sum of all numbers on the _Nth_ row

## Constraints: <br>
 - 1 &le; _N_ &le; 10<sup>4</sup>

## Sample Input: <br>
```
4
```

## Sample Output: <br>
```
60
```

## Explanation: <br>
The 4th row of the triangle is `12 14 16 18`. Sum of all the numbers in the 4th row is 12+14+16+18 = 60. Hence, 60 is the output.

## Solution: <br>
```python
# Take input
n = int(input())
solution = (n-1) * n * (n+1)
print(solution)
```
