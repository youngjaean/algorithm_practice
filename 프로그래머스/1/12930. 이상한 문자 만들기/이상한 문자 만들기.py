def solution(s: str):
    new_string = list(s)
    check_num = 0

    for i, nw in enumerate(new_string):
        if nw == " ":
            check_num = 0
        else:
            if check_num % 2 == 0 and nw.islower():
                new_string[i] = nw.upper()
            elif check_num % 2 != 0 and nw.isupper():
                new_string[i] = nw.lower()
            check_num += 1
    return "".join(new_string)
