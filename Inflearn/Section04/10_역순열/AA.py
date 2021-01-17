#강의 풀이

import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        #자기보다 큰 숫자의 빈 공간을 다 만들어 놨다는 것 and 해당 자리가 비어있으면
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1
            break#j를 break하는 것. 자기 자리 찾았으면 더 돌 필요는 없기 때문
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')

# 인프런 다른 풀이
n = int(input())

a =list(map(int,input().split()))

a = a[::-1]

ans=[]

for x in a:

        ans.insert(x,n)
        print('x', x)
        print('n', n)
        print(ans)

        n -=1

print(ans)