#programmers - 전화번호 목록


def solution(phone_book):
    answer = True
    phoneBook = sorted(phone_book)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
    return answer
