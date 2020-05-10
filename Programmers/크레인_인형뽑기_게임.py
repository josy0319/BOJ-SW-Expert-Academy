#Programmers - 크레인_인형뽑기_게임

'''
단순 구현
'''


def solution(board, moves):
    res = 0
    s = []
    board = list(map(list, zip(*board)))
    for i in moves:
        for idx, j in enumerate(board[i-1]):
            if j!=0:
                if len(s)>0 and s[-1] == board[i-1][idx]:
                        res+=2
                        board[i-1][idx]=0
                        s.pop()
                        break
                else:
                    s.append(board[i-1][idx])
                    board[i-1][idx]=0
                    break
    return res
