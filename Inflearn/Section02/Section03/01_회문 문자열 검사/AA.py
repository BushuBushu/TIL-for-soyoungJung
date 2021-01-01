import sys
sys.stdin = open("data/in3.txt", "rt")
def isSame(l):
    # 계속 참인지를 확인하는 가중치. 넣지 않았다가 넣은 이유가 중요!
    cnt = 0
    if len(l) == 1:
        return 'YES'
    for i in range(len(l) // 2):
        if l[i] == l[len(l) - 1 - i]:
            cnt += 1
    if cnt == len(l) // 2:
        return 'YES'
    return 'NO'

N = int(input())

#입력 이렇게 받는게 맞나?
# 입력받은 문자들의 집합
sl = []
for i in range(N):
    s = input()
    sl.append(s.upper())

for i in range(len(sl)):
    print("#%d" %(i + 1), isSame(sl[i]))

# 강의 풀이
'''
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1-j]:
            print("#d NO" % (i + 1))
            break
    else:
        print("#%d YES" %(i + 1))

# 빠른 풀이

if s == s[::-1] 사용하기


'''