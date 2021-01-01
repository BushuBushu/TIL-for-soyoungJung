# 02. 숫자만 추출

## 문제 내용
문자와 숫자를 섞어 입력받은 뒤 그 중 숫자만 출력하는 것. (맨 앞이 0일 경우 무시한다)

| 난이도 | 정답률(\_%) |
| :----: | :---------: |
|        |             |

## 설계(풀이 방식)
### measure
약수 갯수 구하는 함수

### main
1. num
0부터 9까지의 문자열

2. 이중 for문
입력받은 st문자열 중, num에 해당하는 것이 있는 경우 answer에 추가하고, int(answer)하여 0을 없앤다.
```
answer = ''
for s in st:
    for n in num:
        if s == n:
            answer += s
int(answer)
```

## 강의 해설
x.isdecimal() 함수를 이용한다.

## 배운 개념 및 깨달은 점
```
a = '3²' 
print(a.isdigit()) #True
print(a.isdecimal()) #False
print(a.isnumeric()) #True

```
- x.isdecimal()
    주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수이기 때문에 특수문자 중 숫자모양을 숫자로 치지않는다.

- x.isdigit()
    단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환하는 함수. 즉, 숫자처럼 생긴 '모든 글자'를 숫자로 친다.

- x.isnumeric()
    숫자값 표현에 해당하는 문자열까지 인정한다. 제곱근 및 분수, 거듭제곱 특수문자도 isnumeric() 함수는 True를 반환하는 것을 알 수 있다.

## 정리

| 내 코드 (ms) | 빠른 코드 (ms) |
| :----------: | :------------: |
|              |                |

## 고생한 점