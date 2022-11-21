# Garlanding in the FIFA Mars Cup

## Problem Statement: <br>
In order to commemorate the opening ceremony of the FIFA Mars Cup, the organisers decide to give every player a garland of red and green flowers. The organisers of the FIFA Mars Cup want to make sure that all the garlands that they give to the players are beautiful. There are _T_ garlands each consisting of _N_ flowers placed in a cyclic order. Since Martians believe in change, a garland is considered beautiful if no two adjacent flowers are of the same color. To make the garland beautiful you may perform the following operation at most _K_ times:
 - Make two cuts on the rope (not intersecting the flowers) to split the garland
 - Reverse on of the split parts
 - Join the parts again end-to-end

For each garland your task is to find whether you can make a beautiful garland.

## Constraints: <br>
 - 1 &le; _T_ &le; 100
 - 1 &le; _N_ &le; 10<sup>3</sup>

Subtask 1: 50 points
 - _K_ = 1000000000

Subtask 2: 50 points
 - _K_ = 1

## Input Format: <br>
 - The first line contains a single integer _T_
 - The next _T_ testcases contain two lines of input
 - The first line contains two integers _N_ and _K_
 - The second line contains a string _S_ of length _N_ consisting of the characters 'R' and 'G'

## Output Format: <br>
 - For each testcase display "YES" if it is possible to make a beautiful garland and "NO" if it is impossible to make a beautiful garland from the current garland

## Sample input: <br>
```
3
2 1000000000
RG
4 1
RRGG
2 1
RR
```

## Sample output: <br>
```
YES
YES
NO
```

## Solution: <br>
```python
# Loop through all testcases
for _ in range(int(input())):
	# Take input and print sum
	n, k = map(int, input().split())
	s = input()

	r = s.count('R')
	g = s.count('G')

	if r != g:
		print('NO')
		continue

	if k == int(1e9):
		print('YES')
		continue

	a = 0
	b = 0
	for i in range(n - 1):
		if s[i] == s[i + 1]:
			if s[i] == 'R':
				a += 1
			else:
				b += 1
	
	if a == 1 and b == 1:
		print('YES')
	else:
		print('NO')
```
