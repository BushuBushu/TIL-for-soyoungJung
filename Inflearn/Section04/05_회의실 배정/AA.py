import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
maxx = -10000
info = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(info) - 1):
    chk = []
    for j in range(i + 1, len(info)):
        print(i, j)
        if info[i][1] <= info[j][0]:
            chk.append(info[i])
            chk.append(info[j])
    #chk의 중복 제거
    newchk = []
    for v in chk:
        if v not in newchk:
            newchk.append(v)
    print(newchk)
    if len(newchk) > maxx:
        maxx = len(newchk)

print(maxx)

#강의 풀이
#회의가 끝나는 시간을 기준으로 정렬하기, 빨리끝나는 것이 중요하기 때문!(회의 많은것이 관건)

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
    
#소트하기
#디폴트값은 튜플의 앞의 부분의 맞춰 정렬되는 
meeting.sort(key=lambda x : (x[1], x[0]))
#끝나는 시간
et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)