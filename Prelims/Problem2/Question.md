# Roadster to Bugatti?

## Problem Statement: <br>
Elon Musk Reach mars, and takes his Tesla Roadster for a JoyRide! But the moment he switches on the Engine, he realises that his electric car is now a 12.0L W16 with 8 Speed Transmission. HOW??? 
Then he realises mars is nothing but a Real life scene of the movie Tenet. Everything here was inverted! 
Elon, as much as he hates to do so, has asked you for help
Elon now wants you to make a code, which will take each word in a string, and invert each and every WORD of the string.

## Input Format: <br>
- A single line containing space seperated words

## Output Format: <br>
- A string containing the inverted words, but in the same order.

## Constraints: <br>
 - 1 &le; length of string &le; 110

## Sample Input: <br>
```
oY norI nam si !ereht
```

## Sample Output: <br>
```
Yo Iron man is there!
```

## Solution: <br>
```python
def reverse(sen):
    words = sen.split(" ")
    inv = [word[::-1] for word in words]
    strr = " ".join(inv)
    return strr
 
sen = input()
print(reverse(sen))
```
