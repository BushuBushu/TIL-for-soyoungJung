# 소수인지 판별
def isPrime(x):
    y = 0
    for i in range(1, x + 1):
        if x % i == 0:
            y += 1
    if y >= 3:
        return False
    else:
        return True

N = int(input())

summ = 0
for num in range(2, N + 1):
    if isPrime(num):
        #print(num)
        summ += 1


print(summ)

# 1도 소수라고 나오는 단점
#print(isPrime(1))

# 강의 풀이
'''
n = int(input())
ch = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if i == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1

print(cnt)
'''
