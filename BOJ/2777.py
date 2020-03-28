#BOJ - 숫자 놀이

import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    cnt=0
    if n==1:
        print(1)
        continue
    for j in range(9,1,-1):
        while n%j==0:
            cnt+=1
            n=n//j
            
    print(cnt) if n<10 else print(-1)
