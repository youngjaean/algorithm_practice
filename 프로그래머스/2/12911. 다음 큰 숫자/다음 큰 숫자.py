def solution(n):
    current = bin(n)[2:].count("1")
    next_value = n + 1
    while True:
        if bin(next_value)[2:].count("1") == current:
            break
        else:
            next_value += 1
    return next_value