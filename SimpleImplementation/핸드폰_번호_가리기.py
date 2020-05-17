#Programmers - 핸드폰 번호 가리기

'''
간단한 문자열은 정규식 사용하지 않고 덧셈, 곱셈으로 처리
'''

def solution(phone_number):
    answer = '*'
    return answer*(len(phone_number)-4) + phone_number[-4:]
