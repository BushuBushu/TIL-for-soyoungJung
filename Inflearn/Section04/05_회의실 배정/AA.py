import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
maxx = -10000
info = [list(map(int, input().split())) for _ in range(n)]

#가능한 조합 추려내기
# '''
chk = []
for i in range(len(info) - 1):
     #print(info[i])
     if info[i][1] <= info[i + 1][0]:
        chk.append(info[i])
        #print(info[i])
        chk.append(info[i + 1])
     elif info[i][1] <= info[i + 2][0]:
         chk.append(info[i] + info[i + 2])
         

print(chk)
print(info)
info = [item for item in info if item not in chk] 
# '''
chk = []
for i in range(len(info) - 1):
     #print(info[i])
     if info[i][1] <= info[i + 1][0]:
        chk.append(info[i])
        #print(info[i])
        chk.append(info[i + 1])
print('00000')
print(chk)
print(info)
