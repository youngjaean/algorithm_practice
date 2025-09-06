def solution(n, lost, reserve):
    students = [0] + [1] * n
    lost.sort()
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1

    for i in lost:
        if i != 1 and students[i - 1] > 1:
            students[i] = 1
            students[i - 1] -= 1
        elif i != n and students[i + 1] > 1:
            students[i] = 1
            students[i + 1] -= 1

    while 0 in students:
        students.remove(0)
    return len(students)