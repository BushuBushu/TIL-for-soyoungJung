n = int(input())

a = 0
i = 0
while a // n == 0 and len(str(a)) == a:
    i += 1
    a = a * i
    
print(a)
    
#강의 풀이
#배수를 실제로 만들지 않고 해결한다.(배수가 커지면 시간 복잡도가 커짐)
#n을 나눈 나머지가 0이면, 해당 숫자는 n의 배수. 어떤 수인지는 관심 x

while True:
    try:
        n = int(input())
    except:
        break
    num = 0
    #수의 길이 1부터 시작
    i = 1
    while True:
        #이전 수를 이용해서 다음 수를 만들어 주기. 이전 
        num = num * 10 + 1
        #n으로 나눈 나머지 구하기.
        num = num % n
        #n의 배수임.
        if num == 0:
            print(i)
            break
        #자릿수가 증가
        i += 1
