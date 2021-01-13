import sys
#sys.stdin = open('input.txt', 'r')

N = int(input())

info = []
for _ in range(N):
    h, w = map(int, input().split())
    info.append((h, w))

info.sort(reverse = True)
#print(info)

hmax = info[0][0]
wmax = info[0][1]
cnt = 1


for i in range(1, N):
    if info[i][1] > wmax:
        cnt += 1
        wmax = info[i][1]
        #print(info[i], wmax, "fail")

print(cnt)

#강의 풀이 == 나의 풀이!!
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse = True)
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)