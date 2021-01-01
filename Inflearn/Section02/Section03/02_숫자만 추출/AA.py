#약수 구하기 함수
def measure(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    return cnt

num = '0123456789'

st = input()

answer = ''
for s in st:
    for n in num:
        if s == n:
            answer += s

answer = int(answer)

print(answer)
print(measure(answer))

# 강의 풀이
'''
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt+=1
print(cnt)
'''