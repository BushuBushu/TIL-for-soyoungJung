'''def avg(l):
    summ = 0
    for s in l:
        summ += s
    avg = round(summ / len(l))
    return avg

N = int(input())

#점수 받기
scores = list(map(int, input().split()))
#scores.sort(reverse = True) 소팅하면 학생번호가 이상해짐.

avg = avg(scores)

#평균에 가까운 점수 찾기
diff = []
for score in scores:
    diff.append(abs(avg - score))

print(diff)
# 최소값이 여러개인 경우
if diff.count(min(diff)) > 1:
    # 
stu = diff.index(min(diff))
#answer = scores[stu] + 1

print(avg, stu + 1)

'''
N = int(input())
scores = list(map(int, input().split()))
avg = round(sum(scores) / N)

minn = float('inf')

for idx, x in enumerate(scores):
    tmp = abs(avg - x)
    if tmp < minn:
        minn = tmp
        score = x
        index = idx + 1
    elif tmp == minn:
        if x > score:
            score = x
            index = idx + 1
            
print("%d %d" %(avg, index))
