x, y = map(int, input().split())
grounds = list(map(int, input().split()))

result = 0

for i in range(1, y - 1):
    max_left = max(grounds[: i + 1])
    max_right = max(grounds[i:])
    min_value = min(max_left, max_right)
    result += abs(grounds[i] - min_value)


print(result)
