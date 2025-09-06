total = 0
max_peple = 0
for _ in range(10):
    out_p, in_p = map(int, input().split())
    total -= out_p
    total += in_p
    if max_peple < total:
        max_peple = total

print(max_peple)
