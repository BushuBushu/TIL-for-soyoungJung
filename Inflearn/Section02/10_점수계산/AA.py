N = int(input())
results = [0] + list(map(int, input().split()))

scores = [0] * (1 + N)
for i in range(1, N + 1): #여기서 왜 n + 1인가? 마지막까지 확인하기 위해서! 앞에 0을 하나 추가했기 때문에.
    # 해당 인덱스의 앞 채점이 0이라면
    if results[i - 1] == 0 and results[i] == 1:
        scores[i] = 1
    elif results[i - 1] == 1 and results[i] == 1:
        scores[i] = scores[i - 1] + 1
#print('results',results)
#print('scores', scores)
print(sum(scores))

# 강의 풀이
'''
n = int(input())
a = list(map(int, input().split()))

# 점수의 합
sum = 0

# 가중치
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt #sum에 가중치를 더하기
    else:
        cnt = 0 # cnt를 0으로 다시 초기화 하기

print(sum)
'''

        

