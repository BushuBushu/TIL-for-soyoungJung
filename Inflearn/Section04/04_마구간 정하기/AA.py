import sys
#sys.stdin = open('input.txt','r')
'''
def Check(midd):
    for i in range(2, len(zero + 1)):
        if zero[i] == 1:
            

N, C = map(int, input().split())

xi = []
for _ in range(N):
    xi.append(map(int, input().split()))

#x좌표의 가장 큰 부분까지의 리스트
zero = [0] * (max(xi) + 1)
#1번째 인덱스가 1이라면, x1번째 마구간
for i in xi:
    zero[i] = 1
    
lt = 1
rt = max(xi)
answer = 0

zero[1] = 2
while lt >= rt:
    mid = (lt + rt) // 2
    if Check(mid):
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1
'''        
def Count(distance):
    #처음 배치한 말의 수, 즉 line[0]에 배치한 말
    cnt = 1
    #거리를 재기 시작할 좌표의 위치. 처음 배치된 말부터 시작한다.
    endpoint = line[0]
    for i in range(1, N):
        #if 논리가 너무 이해안된다 ㅠㅜ
        #distance보다 크면, 마구간을 하나 놓을 수 있는 것이 생김..?!
        #distance는 가장 가까운 말의 거리. 즉 그보다 작으면 안됨.
        #distance보다큰 경우에는 말을 놓을 수 있음. 왜냐 그 거리보다 클 수 있는 경우가 있기 때문!
        if line[i] - endpoint >= distance:
            cnt += 1
            endpoint = line[i]
        #else이면,  가버리면 다음 i로 넘어가기
    return cnt
        

N, C = map(int, input().split())

line = []
for _ in range(N):
    line.append(int(input()))
line.sort()

lt = 1
rt = line[-1] - line[0]

res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= C:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
    