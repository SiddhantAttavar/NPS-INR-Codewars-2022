from random import randint

def generate(subtask):
    mat = []
    n = randint(0, 20)
    m = randint(0, 20)
    for i in range(n):
        temp = []
        for k in range(m):
            temp.append(randint(0, 9))
        mat.append(temp)
        




if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))