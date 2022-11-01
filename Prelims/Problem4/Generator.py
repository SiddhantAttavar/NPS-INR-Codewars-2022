import random
import string

def generate(subtask):
    strr = ""
    words = random.randint(0, 10)
    for i in range(words):
        N = random.randint(0, 10)
        res = ''.join(random.choices(string.ascii_letters, k=N))
        strr = strr + res + " "
    strr = strr.strip()
    print(strr)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))