from collections import deque


def adjust(word, next_word):
    count = 0
    for w1, w2 in zip(word, next_word):
        if w1 != w2:
            count += 1
        if count > 1:
            return False
    return True


def solution(begin, target, words):
    if target not in words:
        return 0
    que = deque([(begin, 0)])
    visitted = [begin]

    while que:
        current_word, level = que.popleft()
        if current_word == target:
            return level
        for word in words:
            if word not in visitted and adjust(current_word, word):
                visitted.append(word)
                que.append((word, level + 1))