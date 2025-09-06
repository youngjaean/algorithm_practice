N, K = map(int, input().split())
i = 1
mdeicin_list = []
while i <= N:
    if N % i == 0:
        mdeicin_list.append(i)
        if len(mdeicin_list) >= K:
            break

    i += 1

if len(mdeicin_list) >= K:
    print(mdeicin_list[K - 1])
else:
    print(0)
