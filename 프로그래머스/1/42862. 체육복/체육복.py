def solution(n, lost, reserve):
    students = [1] * n
    for l in lost:
        students[l - 1] -= 1
    for r in reserve:
        students[r - 1] += 1
    if students[0] == 0:
        if students[1] > 1:
            students[0] = 1
            students[1] -= 1
    for i in range(1, len(students) - 1):
        if students[i] == 0:
            if students[i - 1] > 1:
                students[i] = 1
                students[i - 1] -= 1
            elif students[i + 1] > 1:
                students[i] = 1
                students[i + 1] -= 1
    if students[-1] == 0:
        if students[-2] > 1:
            students[-1] = 1
            students[-2] -= 1
    while 0 in students:
        students.remove(0)
    return len(students)
