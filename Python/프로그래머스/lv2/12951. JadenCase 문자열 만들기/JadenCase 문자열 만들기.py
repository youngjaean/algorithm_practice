def solution(s):
    s = s.lower()
    answer = ""
    for i, c in enumerate(s):
        if i == 0:
            answer += s[0].upper()
        else:
            if s[i - 1] == " ":
                answer += s[i].upper()
            else:
                answer += s[i]

    return answer