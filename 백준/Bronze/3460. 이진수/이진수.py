n = int(input())
for _ in range(n):
    binary_num = str(bin(int(input()))).replace("0b", "")[::-1]

    for i, num in enumerate(binary_num):
        if num == "1":
            print(i, end=" ")
    print()
