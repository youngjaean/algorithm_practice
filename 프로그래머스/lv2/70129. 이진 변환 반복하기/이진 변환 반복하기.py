def solution(s):
    count = 0
    repate = 0
    while s != "1":
        count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s)).replace("0b", "")
        repate += 1
    return [repate, count]