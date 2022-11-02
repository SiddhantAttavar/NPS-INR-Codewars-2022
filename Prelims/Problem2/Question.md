# Problem 2
## Problem Statement
Doreamon and Nobita use Doreamon's 4D pocket to teleport to Mars. Interestingly, they find all numbers in Mars written in binary! <br/>
Make a code to convert the binary into numbers, so that nobita can finally buy his Gukki and Louis Button Wallet...

## Explanation
For those who are not familiar with binary, it works in the powers of 2. For eg, in 101, the right most number [1] stands for 2^0x1, and the middle number [0] stands for 2^1x0, and the leftmost number [1] stands for 2^2x1
Hence, 101 is 2^2x1 + 2^1x0 + 2^0x1 = 5+0+1 = 6
The same way, 10101 = 2^4x1 + 2^3x0 + 2^2x1 + 2^1x0 + 2^0x1 = 16+0+4+0+1 = 21

## Input Format
It will be inputed as a string, 
1001

## Output Format
As an integer, 
9

## Sample Input
1011

## Sample Ouput
11

## Constraints
 The answer should only be executed in the form of an integer, not a string or array.

