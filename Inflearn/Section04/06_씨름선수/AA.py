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