#내 풀이
import sys
#sys.stdin = open('input.txt' ,'r')

n = int(input())

dis = [[100] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dis[i][i] = 0

for i in range(n):
    a, b = map(int, input().split())
    #무방향그래프이기 때문에
    dis[a][b] = 1
    dis[b][a] = 1
    if a == -1 or b == -1:
        break
    
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
''' 이 부분이 너무 더러움 ㅠ

#100을 -1로 다시 바꾸기 -> 각 행의 최대값을 찾을 수 있도록
for i in range(n + 1):
    for j in range(n + 1):
        if dis[i][j] == 100:
            dis[i][j] = -1

minn = 500
li = []
for i in range(1, n + 1):
    li.append(max(dis[i]))
    
a = min(li)
cnt = 0
for i in li:
    if i == a:
        cnt += 1
print(a, cnt)

for i in range(n):
    if li[i] == a:
        print(i + 1, end = ' ')
'''
#강의 부분 ==> 최대한 효율적으로 짜보기!!
res = [0] * (n + 1)
#최솟값을 찾는 것이기 때문에 최댓값으로 초기화
score = 100
for i in range(1, n + 1):
    for j in range(1, n + 1):
        #각 후보의 점수
        res[i] = max(res[i], dis[i][j])
    score = min(score, res[i])

out = []
for i in range(1, n + 1):
    if res[i] == score:
        #회장 후보의 번호가 out에 들어감.
        out.append(i)
#out의 len이 후보들의 수 임.
print("%d %d" %(score, len(out)))
for x in out:
    print(x, end = ' ')
