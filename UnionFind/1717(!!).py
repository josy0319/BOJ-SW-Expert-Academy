# BOJ - 집합의 표현

'''
disjoint-set -> Union-Find 자료구조
원소가 같은 루트값을 가지는지 효과적으로 체크해주는 구조
'''


def find(x):
    #만약 x의 값이 루트의 값이 아니라면
    if parent[x] != x:
        #루트 값을 재귀적으로 찾음
        #찾으면서 중간 다리를 해주는 노드들의 값도 루트 값으로 변경해줌 
        parent[x] = find(parent[x])
    #루트 값이었다면 그냥 반환, 아니였다면 루트 값을 찾은 후 반환
    return parent[x] 

def union(a, b):
    #a와 b의 루트 값을 찾은 후 저장
    root1 = find(a)
    root2 = find(b)
    #비교해서 서로 다른 값이라면
    if root1 != root2:
        #큰 수를 루트노드로 지정
        if root1 > root2:
            parent[root2] = root1
        else:
            parent[root1] = root2

n, m= map(int, input().split())
parent= [i for i in range(n+1)]

for i in range(m):
    bit, a, b= map(int, input().split())
    if bit:
        #find값이 같다면 동일 루트 값을 가지고 있음(즉, 같은 영역 union이 된 상태)
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        #a와 b값을 합쳐줌(Union)
        union(a, b)

