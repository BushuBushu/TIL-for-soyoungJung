# 04. 두 리스트 합치기

## 문제 내용
 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력

| 난이도 | 정답률(\_%) |
| :----: | :---------: |
|        |             |

## 설계(풀이 방식)
두 리스트를 합치고 sort하기

## 강의 해설
![image](https://user-images.githubusercontent.com/68037174/103439324-3d6c5700-4c7f-11eb-9a9c-63e0adb3e2bc.png)

p1과 p2는 인덱스 값이고, a와 b 리스트의 값을 비교하여 작을 경우 c 리스트에 append시키기. 하나의 리스트가 c에 모두 넣어졌다면, 나머지 리스트의 값은 그대로 slicing해서 넣기

## 배운 개념 및 깨달은 점
- sort()의 시간 복잡도
    O(N Log N)
- 이미 정렬되어 있는 것들을 합치는 경우, N번만에 완료할 수 있다.


## 정리

| 내 코드 (ms) | 빠른 코드 (ms) |
| :----------: | :------------: |
|              |                |

## 고생한 점