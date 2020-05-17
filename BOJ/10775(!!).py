#BOJ - 공항

'''
Union-Find 응용 문제

시간초과 발생하면 한번 생각해 볼 유형
'''



def find(num):
    if parent[num] != num:
        parent[num] = find(parent[num])
    return parent[num] 

def union(num1,num2):
    root1 = find(num1)
    root2 = find(num2)
    parent[root1] = root2

res = 0
g = int(input())
#0을 이용한다.
parent = [i for i in range(g+1)]
for p in range(int(input())):
    ap = int(input())
    #도킹할 게이트를 찾는다
    num = find(ap)
    #게이트가 0이 아니라면
    if num != 0:
        #num-1과 union
        union(num,num-1)
        res+=1
    else:
        break
print(res)
