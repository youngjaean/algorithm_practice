def solution(genres, plays):
    genrs_dict = {}

    for genr, play in zip(genres, plays):
        try:
            genrs_dict[genr].append(play)
        except:
            genrs_dict[genr] = [play]
    sum_list = []

    for key in genrs_dict.keys():
        sum_list.append([key, sum(genrs_dict[key])])
    sum_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for key in sum_list:
        for x in sorted(genrs_dict[key[0]], reverse=True)[:2]:
            answer_index = plays.index(x)
            answer.append(answer_index)
            plays[answer_index] = -1
    return answer
