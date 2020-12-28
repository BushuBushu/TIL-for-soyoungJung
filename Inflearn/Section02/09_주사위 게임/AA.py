# 규칙 정의하기, 하나의 리스트를 파라미터로)
def rule(l):
    for i in range(len(l)):
        if l.count(l[i]) == 3:
            eye = l[i]
            prize = 10000 + eye * 1000
            return prize
        elif l.count(l[i]) == 2:
            eye = l[i]
            prize = 1000 + eye * 100
            return prize
        else:
            eye = l[i]
            prize = max(l) * 100
            return prize
#여기서 뭔가 규칙성을 찾을 수 있을까?
#  '''
N = int(input())
dl = []
for x in range(N):
    dice = list(map(int, input().split()))
    dl.append(dice)

# print(dl)
# ''''

prizes = []
for p in dl:
    prizes.append(rule(p))

print(max(prizes))

# 강의 풀이
'''
n = int(input())

res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp) #각자의 값을 받았음.

    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    if money > res:
        res = money

print(res)
'''