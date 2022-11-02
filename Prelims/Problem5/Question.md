# Sample Problem

## Problem Statement: <br>
The Supreme Hon'ble head of state of the Democratic People's Republic of Mars has a very busy schedule. He has _N_ appointments on his calendar. However since some of them overlap, it is impossible for him to attend all these appointments. Therefore, he wants to select a subset of these _N_ appointments. The _ith_ event begins at time _S<sub>i</sub>_ and ends at time _T<sub>i</sub>_. Your task is to find the maximum number of appointments that the head of state can attend without any overlapping appointments.

## Constraints: <br>
 - 1 &le; _S<sub>i</sub>_, _B<sub>i</sub>_ &le; 10<sup>9</sup>
 - 1 &le; _N_ &le; 10<sup>5</sup>

Subtask 1: 20 points
 - 1 &le; _N_ &le; 15

Subtask 2: 10 points
 - _S<sub>i</sub>_ == _T<sub>i</sub>_

Subtask 3:
 - No additional constraints

## Input Format: <br>
 - The first line contains a single integer _N_
 - The next _N_ lines contain two integers _S<sub>i</sub>_ and _T<sub>i</sub>_

## Output Format: <br>
 - Print a single line containing the maximum number of events the head of state can attend

## Sample input: <br>
```
4
1 3
2 5
3 9
6 8
```

## Sample output: <br>
```
2
```

## Explanation: <br>
If we select the first appointment, it gets over at time 3. Then we cannot select either the second or third appointment as they overlap with the first one. The only appointment we can select is the fourth one.

It can be shown that there is no way to select 3 or more appointments without overlap.
