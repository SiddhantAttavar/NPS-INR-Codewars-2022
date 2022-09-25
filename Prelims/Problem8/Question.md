# Connecting Mars

## Problem Statement: <br>
The democratic sovereign peoples republic of Mars is very corrupt. Five years ago they promised that they would build big highways connecting every major city on Mars but they have still not delivered on that promise. The people are now protesting about the poor transportation infrastructure, so the government has finally decided to build the roads. However since the president wants to keep all the taxpayers money for himself, he plans on using as little money as possible to build the roads. To help him out, he calls you to find out the least amount of money required to connect every city on Mars.

There are _N_ cities on Mars and _M_ potential roads that can be built between these cities. For each potential road, you are given 3 integers, the starting city, the ending city and the cost to build that road. The roads are bidirectional, i.e. the road used to travel from city _U_ to city _V_ can also be used to travel from city _V_ to city _U_.

## Constraints: <br>
 - 1 &le; _M_ &le; min(10<sup>5</sup>, _N_ * (_N_ + 1) / 2)
 - 0 &le; _U<sub>i</sub>_, _V<sub>i</sub>_ &le; _N_
 - 0 &le; _W<sub>i</sub>_ &le; 10<sup>9</sup>

Subtask 1: 20 points
 - 1 &le; _N_ &le; 15

Subtask 2: 30 points
 - 1 &le; _N_ &le; 100

Subtask 3: 50 points
 - 1 &le; _N_ &le; 10<sup>5</sup>

## Input Format: <br>
 - The first line contains two integers _N_ and _M_
 - The next _M_ lines contain three integers _U<sub>i</sub>_, _V<sub>i</sub>_ and _W<sub>i</sub>_ (_U<sub>i</sub>_ is the starting city, _V<sub>i</sub>_ is the ending city and _W<sub>i</sub>_ is the cost of building the road)

## Output Format: <br>
 - Print a single line for each testcase containing the least amount of money required to connect all the cities. If the cities cannot be connected print -1

## Sample input: <br>
```
3 4
1 3 5
3 2 6
1 2 2
3 1 9
```

## Sample output: <br>
```
7
```
