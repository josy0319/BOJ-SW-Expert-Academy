#Programmers - 프렌즈4블록

'''
그래프 중력
값을 변경하여 유지하는 것보다는 
새로운 리스트를 만들어 활용하는 것 -> 활용도가 높다 
'''

#1차시기, 2개 케이스 불만족
def solution(m, n, board):
    res = 0
    board = [list(i) for i in board]
    for i in board:
        print(i)
    print()
    for x in range(20):
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j].isalpha() and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    board[i][j] = '0'
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    if board[i+1][j] != '0':
                        board[i+1][j] = '1'
                    if board[i][j+1] != '0':
                        board[i][j+1] = '1' 
                    if board[i+1][j+1] != '0': 
                        board[i+1][j+1] ='1'

        for i in range(m-1):
            for j in range(n):
                if board[i+1][j].isdigit():
                    board[i+1][j] = '3'
                    board[i+1][j], board[i][j] = board[i][j],board[i+1][j]
    for i in board:
        print(i)
    
    for i in board:
        for j in range(n):
            if i[j].isdigit():
                res+=1
    return res



#2차시기
def solution(m, n, board):
    board = [list(i) for i in board]
    
    while True:
        visited = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] == board [i][j+1] == board[i+1][j+1]:
                    visited.append((i,j))
                    visited.append((i+1,j))
                    visited.append((i,j+1))
                    visited.append((i+1,j+1))
        if len(visited) == 0:
            break
        visited = list(set(visited))
        for x, y in visited:
            board[x][y] = 0
        
        for i in range(m-1,0,-1):
            for j in range(n):
                if board[i][j]==0:
                    for k in range(i-1,-1,-1):
                        if board[k][j] != 0 :
                            break
                    board[i][j], board[k][j] = board[k][j], board[i][j]
    return sum(i.count(0) for i in board)
