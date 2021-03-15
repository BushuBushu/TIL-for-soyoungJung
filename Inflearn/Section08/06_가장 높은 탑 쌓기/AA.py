import sys
sys.stdin = open('input.txt', 'r')

bn = int(input())
bi = [list(map(int, input().split())) for _ in range(bn)]
bi.insert(0, [0, 0, 0])
#bi.sort(key = lambda x:x[0])
d = [0] * (bn + 1)
d[1] = bi[1][1]


for i in range(2, bn + 1):
    maxx = 0
    for j in range(i - 1, 0, -1):
        if bi[j][2] > bi[i][2] and d[j] > maxx:
            maxx = d[j]
    d[i] = maxx + bi[i][1]

print(max(d))

#강의 풀이
#d[2]는 2번 벽돌을 가장 꼭대기에 놓았을 때의 최대 높이.
# 밑면의 넓이를 내림차순으로 하고, 무게만 비교하도록.
import sys
sys.stdin = open('input.txt', 'r')

bn = int(input())
bi = [list(map(int, input().split())) for _ in range(bn)]
#bi.insert(0, [0, 0, 0])
bi.sort(reverse = True)
#print(bi)
d = [0] * bn
d[0] = bi[0][1]
res = bi[0][1]

for i in range(1, bn):
    maxx = 0
    for j in range(i - 1, -1, -1):
        if bi[j][2] > bi[i][2] and d[j] > maxx:
            maxx = d[j]
    d[i] = maxx + bi[i][1]
    res = max(res, d[i])

print(res)