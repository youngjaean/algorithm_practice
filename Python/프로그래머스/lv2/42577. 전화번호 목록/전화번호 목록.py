def solution(phone_book):
    phone_book = sorted(phone_book)
    for num, check in zip(phone_book, phone_book[1:]):
        if check.startswith(num):
            return False
    answer = True
    return answer
