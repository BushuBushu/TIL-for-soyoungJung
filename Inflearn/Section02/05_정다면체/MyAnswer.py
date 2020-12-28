# 모든 면 구하기 # 어려움 ㅠ 내 방법이 왜 안될까ㅏ
N, M = map(int, input().split())

Nl = []
Ml = []
for n in range(N):
    Nl.append(n + 1)

for m in range(M):
    Ml.append(m + 1)

l = Nl + Ml

# print('L',l)

# 모든 눈의 합 경우의 수 구하기 ?? 여기서는 왜 5가 포함이 안되지?? ㅠㅜ..
summs = []

for x in range(len(l)):
    for y in range(x + 1, len(l)):
        summs.append(l[x] + l[y])

#summs.sort()
#print('summs', summs)
        
# 경우의 수에서 출현할 확률이 높은 수 찾기
pers = set()


'''
maxx = 0
for i in range(len(summs)):
    per = summs.count(summs[i]) / len(summs)
    tmp = per
    if tmp > maxx:
        maxx = tmp
        
    

'''


for i in range(len(summs)):
    per = summs.count(summs[i]) / len(summs)
    pers.add(per)

#print(pers)

maxx = max(pers)
#print(maxx)

answer = set()

for j in range(len(summs)):
    per2 = summs.count(summs[j]) /len(summs)
    if per2 == maxx:
        answer.add(summs[j])

for a in answer:
    print(a, end = ' ')
        

# 왜 틀리지? 모든 합을 ㅡ구하는 것이 틀렸나?
# 코드가 너무 더러움.. ㄷ듀 
        
