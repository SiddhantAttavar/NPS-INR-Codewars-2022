# Sample Problem

## Problem Statement: <br>
Finally, after years of anticipation, the first basketball court has been opened on Mars, so the governor has decided to hold a basketball exercise session. 2⋅n students have come to the governor's exercise session, and he lined up them into two rows of the same size (there are exactly _N_ people in each row). Students are numbered from 1 to _N_ in each row in order from left to right.

```
1 2 3 4 5 ... n
1 2 3 4 5 ... n
```

Now the governor wants to choose a team to play basketball. He will choose players from left to right, and the index of each chosen player (excluding the first one taken) will be strictly greater than the index of the previously chosen player. To avoid giving preference to one of the rows, the governor chooses students in such a way that no consecutive chosen students belong to the same row. The first student can be chosen among all _2N_ students (there are no additional constraints), and a team can consist of any number of students.

The governor thinks, that in order to compose a perfect team, he should choose students in such a way, that the total height of all chosen students is maximum possible. Help the governor to find the maximum possible total height of players in a team he can choose.

## Constraints: <br>
 - 0 &le; _A<sub>i</sub>_, _B<sub>i</sub>_ &le; 10<sup>9</sup> (1 &le; _i_ &le; _N_)

Subtask 1: (20 points)
 - 1 &le; _N_ &le; 15

Subtask 2: (80 points)
 - 1 &le; _N_ &le; 10<sup>5</sup>

## Input Format: <br>
 - The first line contains a single integer _N_
 - The next line contain _N_ integers representing the heights in _A_
 - The next line contain _N_ integers representing the heights in _B_

## Output Format: <br>
 - Print a single line for each testcase containing the maximum sum of heights

## Sample input: <br>
```
5
9 3 5 7 3
5 8 1 4 5
```

## Sample output: <br>
```
29
```
