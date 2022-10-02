# To The Moon!

## Problem Statement: <br>
X Æ A-15 Musk, the richest person on Mars, is an avid investor. His army of Tesla Bots has devised an algorithm to accurately predict the share price of Frozen Banana Corporation (FBC) for the next few days. Now unstoppable, he has decided to invest in FBC and wants to know the maximum profit he can make by buying and selling the stock.

Each day, he can either buy one share of FBC, sell any number of shares of FBC that he owns, or not make any transaction at all. What is the maximum profit he can obtain with an optimum trading strategy?

## Input Format: <br>
- The first line contains the number of test cases _T_.
- For each of the _T_ test cases:
    - The first line contains an integer _N_, the number of days predicted.
    - The second line contains _N_ space-separated integers, _P<sub>i</sub>_, the price of FBC on the _i<sup>th</sup>_ day.

## Output Format: <br>
For each test case, output a single line containing the maximum profit that X Æ A-15 Musk can make.

## Constraints: <br>
- 1 ≤ _T_ ≤ 10
- 1 ≤ _N_ ≤ 5 * 10<sup>4</sup>
- 1 ≤ _P<sub>i</sub>_ ≤ 10<sup>5</sup>

## Sample Input: <br>
```
3
3
5 3 2
3
1 2 100
4
1 3 1 2
```

## Sample Output: <br>
```
0
197
3
```

## Explanation: <br>
For the first case, there is no profit because the share price never rises, return 0.

For the second case, buy one share on the first two days and sell both of them on the third day for a profit of 197.

For the third case, buy one share on day 1, sell one on day 2, buy one share on day 3, and sell one share on day 4. The overall profit is 3.
