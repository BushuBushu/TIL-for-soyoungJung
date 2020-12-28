#x는 스트링으로 받은 자연수
def digit_sum(x):
    summ = 0
    for s in x:
        summ += int(s)
    return summ

N = int(input())
nums = list(input().split())

maxx = 0
for num in nums:
    sum = digit_sum(num)
    if maxx < sum:
        maxx = sum
        answer = num

print(answer)

