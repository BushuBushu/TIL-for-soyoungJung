import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
li = list(map(int, input().split()))

if N // 2 == 0:
    L = li[:]
    R = li[: : -1]
else:
    L = li[:]
    R = li[:: -1]

print(L, R)

nl = []
st = ''

'''
#첫 숫자 비교해서 nl값 초기화 시키기
ls = L[0]
rs = R[0]

if L[0] <= R[0]:
    nl.append(L[0])
    st.append('L')
    ls = L[1]
else:
    nl.append(R[0])
    st.append('R')
    rs  = R[1]
'''    

#반복문 조건 생각하기
for i in range(N // 2):
    if i == 0:
        if L[i] <= R[i]:
            nl.append(L[i])
            st += 'L'
            ls = L[i + 1]
            rs = R[i]
        else:
            nl.append(R[i])
            st += 'R'
            rs = R[i + 1]
            ls = L[i]
    ep = nl[-1]
    if ls > ep:
        if ls <= rs:
            nl.append(ls)
            st += 'L'
            ls = L[i + 1]
        else:
            nl.append(rs)
            st += 'R'
            rs = R[i + 1]
    if rs > ep:
        if rs <= ls:
            nl.append(rs)
            st += 'R'
            rs = R[i + 1]
        else:
            nl.append(ls)
            st += 'L'
            ls = L[i + 1]
            
print(nl)
            
#강의 풀이

n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n - 1
last = 0
res = ''
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    # 둘 중 작은 값을 증가수열로 먼저 추가함
    tmp.sort()
    #tmp에 아무런 값이 들어가지 않았다면, 더이상 가져올 값이 없는 것! 즉, 왼쪽과 오른 쪽 모두 last보다 작은 경우일 때는 종료됨.
    if len(tmp) == 0:
        break
    else:
        #sort한 값 중 작은 값을 추가시키기
        res += tmp[0][1]
        last = tmp[0][0]
        #left인지 right인지에 따라 lt, rt를 움직여 줘야 함.
        if tmp [0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)

