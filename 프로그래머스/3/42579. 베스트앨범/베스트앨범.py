from collections import defaultdict


def solution(genres, plays):
    answer = []
    gen_dict = defaultdict(list)
    play_sum = defaultdict(int)
    for gn, pl in zip(genres, plays):
        gen_dict[gn].append(pl)
        play_sum[gn] += pl
    for key in sorted(play_sum.keys(), key=lambda x: play_sum[x], reverse=True):
        for value in sorted(gen_dict[key], key=lambda x: x, reverse=True)[0:2]:
            index = plays.index(value)
            answer.append(index)
            plays[index] = -1
    return answer