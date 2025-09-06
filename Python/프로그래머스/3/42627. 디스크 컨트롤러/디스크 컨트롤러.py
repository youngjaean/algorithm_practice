import heapq


def solution(jobs):
    answer, now = 0, 0
    pre_start = -1
    line = []
    i = 0
    while i < len(jobs):
        for start, end in jobs:
            if pre_start < start <= now:
                heapq.heappush(line, [end, start])
        if len(line) > 0:
            current_end, current_start = heapq.heappop(line)
            pre_start = now
            now += current_end
            answer += now - current_start
            i += 1
        else:
            now += 1

    return int(answer // len(jobs))
