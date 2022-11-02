def reverse(sen):
    words = sen.split(" ")
    inv = [word[::-1] for word in words]
    strr = " ".join(inv)
    return strr
 
sen = input()
print(reverse(sen))
