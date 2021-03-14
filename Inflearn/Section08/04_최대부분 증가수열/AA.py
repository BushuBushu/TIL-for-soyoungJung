#내 풀이
import sys
#sys.stdin = open('input.txt', 'r')

n = int(input())
li = list(map(int, input().split()))
li.insert(0, 0)

d = [0] * (n + 1)
d[1] = 1

for i in range(2, n + 1):
    if li[i] > li[i - 1]:
        d[i] = d[i - 1] + 1
    else:
        for j in range(1, i):
            if li[i] > li[j]:
                d[i] = d[j] + 1
            else:
                d[i] = d[j]

print(d[n])
        
#강의 풀이
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
#dy의 인덱스의 해당 수를 끝 수로 뒀을 때 나올 수 있는 증가수열의 값 중 최대값
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2, n+1):
    #끝점으로 뒀을 때 나올 수 있는 증가수열은 많음. 그 중 최대를 찾는 것.
    max=0
    #i숫자 전까지 모두 탐색하는데 "거꾸로" 탐색함. 
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    #dy의 마지막 인덱스가 아니라 , 그 중에서 가장 큰 값을 꺼내야 함.
    if dy[i]>res:
        res=dy[i]
print(res)