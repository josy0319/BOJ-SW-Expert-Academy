
#BOJ - 친구 네트워크

'''
disjoint-set 응용
Union-Find자료구조에 Dict자료구조 응용
'''


def find(x):
    #만약 x의 루트가 본인이 아니라면
    if name[x] != x:
        #루트를 재귀적으로 찾음
        name[x] = find(name[x])
    #루트를 반환
    return name[x]
def union(x,y):
    #x,y 값의 루트 값을 가져오고
    root1 = find(x)
    root2 = find(y)
    #만약 서로 루트가 다르다면
    if root1 != root2:
        #y값의 루트를 x의 루트로 치환
        name[root2] = root1
        #y값의 네트워크를 x값의 네트워크에 더해줌
        seq[root1]+=seq[root2]

for i in range(int(input())):
    f = int(input())
    name = dict()
    seq = dict()
    for j in range(f):
        a,b = input().split()
        #a와 b가 name딕셔너리와 seq딕셔너리에 없다면 초기화
        if a not in name:
            name[a] = a
            seq[a] = 1
        if b not in name:
            name[b] = b
            seq[b] = 1
        #union함수로 친구 네트워크 형성
        union(a,b)
        #a의 친구 네트워크 수 출력
        print(seq[find(a)])
