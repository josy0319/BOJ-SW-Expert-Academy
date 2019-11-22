#문자열 다루기 기본

import re
def solution(s):
    answer = True
    p = re.compile('[a-z]')
    m = p.search(s)
    if m == None and (len(s) == 4 or len(s) == 6):
        answer = True
    else :
        answer = False
    return answer
