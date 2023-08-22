def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divisorsList.append(i)
            if (i**2) != n:
                divisorsList.append(n // i)

    divisorsList.sort()
    return_list = []
    for div in range(len(divisorsList)):
        return_list.append(
            [divisorsList[div], divisorsList[len(divisorsList) - div - 1]]
        )

    return return_list


def solution(brown, yellow):
    answer = []
    check_list = getMyDivisor(brown + yellow)

    for number in check_list:
        if (number[0] - 2) * (number[1] - 2) == yellow:
            answer = number
            break
    answer.sort(reverse=True)
    return answer
