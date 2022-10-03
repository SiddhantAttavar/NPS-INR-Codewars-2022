from random import randint

def generate(subtask):
    # Print T
    t = randint(1, 10)
    print(t)

    for i in range(t):
        # Print N
        n = randint(1, int(5e4))
        print(n)

        for j in range(n):
            # Print P_i
            print(randint(1, int(1e5)), end=' ')
        print()

if __name__ == '__main__':
    generate(int(input('Enter the subtask: ')))
