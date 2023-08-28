def move(start, to):
    print(start, to)


def hanoi(N, start, to, via):
    if N == 1:
        move(start, to)
    else:
        hanoi(N - 1, start, via, to)
        move(start, to)
        hanoi(N - 1, via, to, start)


n = int(input())
print(2**n - 1)
hanoi(n, "1", "3", "2")