from collections import deque


def solution(A, B):
    A = deque(sorted(A))
    B = deque(sorted(B))

    answer = 0
    while B:
        if A[0] < B[0]:
            A.popleft()
            B.popleft()
            answer += 1
        else:
            B.popleft()
    return answer