# BOJ - 17836
# python - bfs문제

'''
* 전역변수 Global선언
* list의 스택/큐 활용
* bfs에서
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    ->이동할 수 리스트로 저장 활용

'''

def bfs():  
    q = []
    global result
    visited[0][0] = 1
    q.append((0,0))
    while q:
        x,y = q.pop(0)
        if maze[x][y] == 2:
            result = info[0]-1-x + info[1]-1-y + visited[x][y]-1
        if x==info[0]-1 and y== info[1]-1:
            return min(visited[x][y]-1, result)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<info[0] and 0<=ny<info[1] and maze[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return result

if __name__ == "__main__":
    result = 1000000
    info = list(map(int,input().split()))
    maze = []
    for i in range(info[0]):
        maze.append(list(map(int,input().split())))
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[0]*info[1] for _ in range(info[0])]
    res = bfs()

    print("Fail" if(res>info[2]) else res)




   
