import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
d = [0] * (n + 1)

d[1] = 1
d[2] = 2
for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])

