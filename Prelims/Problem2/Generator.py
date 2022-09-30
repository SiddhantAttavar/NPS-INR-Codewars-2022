import random
def generate(subtask):
    temp = []
    r = random.randint(1,12)
    for i in range(r):
        l = random.randint(0,1)
        temp.append(l)

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
