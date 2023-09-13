from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
sum_, sub_, mul, div_ = map(int, input().split())

# 생각의 발전이 안됫던것
# 백트레킹 찾아보기
operation = "+" * sum_ + "-" * sub_ + "*" * mul + "/" * div_
operation_per = permutations(operation, N - 1)
max_value = -1e9
min_value = 1e9
for operation in operation_per:
    answer = num_list[0]
    for i in range(1, N):
        if operation[i - 1] == "+":
            answer += num_list[i]
        if operation[i - 1] == "-":
            answer -= num_list[i]
        if operation[i - 1] == "*":
            answer *= num_list[i]
        if operation[i - 1] == "/":
            if answer < 0 and num_list[i] > 0:
                answer = -1 * (answer * (-1) // num_list[i])
            else:
                answer //= num_list[i]

    max_value = max(max_value, answer)
    min_value = min(min_value, answer)

print(int(max_value))
print(int(min_value))
