# 문제번호. 문제제목

## 문제 내용


| 난이도 | 정답률(\_%) |
| :----: | :---------: |
|        |             |

## 설계(풀이 방식)

## 강의 해설

## 배운 개념 및 깨달은 점
> ### itertools 활용하기

- 4가지의 수에서 4개의 요소로 만들 수 있는 순열 구하기

`itertools.permutations(리스트)`
```
import itertools as it
a = [1, 2, 3, 4]
for tmp in it.permutations(a)
print(tmp)
```
- 4가지 수에서 n개의 요소로 만들 수 있는 순열 구하기

`itertools.permutations(리스트, n)`
```
import itertools as it
a = [1, 2, 3, 4]
for tmp in it.permutations(a, n)
print(tmp)
```
## 정리

| 내 코드 (ms) | 빠른 코드 (ms) |
| :----------: | :------------: |
|              |                |

## 고생한 점