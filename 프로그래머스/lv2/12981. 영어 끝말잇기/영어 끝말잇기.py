def solution(n, words):
    last = ""
    for i, w in enumerate(words):
        if last == "":
            last = w[-1]
        else:
            first = w[0]
            if first == last and words[i] not in words[:i]:
                if i + 1 != len(words):
                    last = words[i][-1]
                else:
                    return [0, 0]
            else:
                return [
                    [(i + 1) % n if (i + 1) % n != 0 else n][0],
                    (i // n) + 1,
                ]