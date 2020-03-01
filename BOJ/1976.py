#BOJ - 여행 가자

'''
Disjoint-Set
Union-Find
분리 집합
'''


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    root1 = find(a)
    root2 = find(b)
    if root1 != root2:
        if root1 > root2:
            parent[root2] = parent[root1]
        else:
            parent[root1] = parent[root2]

n = int(input())
m = int(input())

parent = [i for i in range(n)]
for i in range(n):
    info = list(map(int,input().split()))
    for j in range(len(info)):
        if info[j] == 1:
            union(i,j)
            print(parent)
            print(i,j)
   
res = list(map(int,input().split()))
print(parent,res[0])   
ans = find(res[0]-1)
for i in res:
    print(ans, find(i-1))
    if find(i-1) != ans:
        print('NO')
        break
else:
    print('YES')
            
    
