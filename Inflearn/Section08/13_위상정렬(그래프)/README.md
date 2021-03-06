# 문제번호. 문제제목

## 문제 내용


| 난이도 | 정답률(\_%) |
| :----: | :---------: |
|        |             |

## 설계(풀이 방식)

## 강의 해설

## 배운 개념 및 깨달은 점

### 위상정렬

> 개념

    사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 "순서대로 나열"하는 것 ex. 선수과목

> 용어

    - 진입차수: 특정 노드로 들어오는 간선의 개수
    - 진출차수: 특정 노드에서 나가는 간선의 개수
    ![image](https://user-images.githubusercontent.com/68037174/112600113-1c696b80-8e54-11eb-8c09-e6be7759c955.png)


> 큐를 이용한 위상 정렬 알고리즘의 동작 과정

    - `graph`: 방향 크래프를 저장하는 2차원 테이블
    - `degree`: 진입차수를 저장하는 리스트

    1. 진입차수가 0인 노드를 큐에 넣기
    2. 큐가 빌 때까지 반복
        a. 큐에서 노드를 꺼내고, 해당 노드에서 나가는 간선의 진입차수를 감소시킨다.
        b. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

## 정리

| 내 코드 (ms) | 빠른 코드 (ms) |
| :----------: | :------------: |
|              |                |

## 고생한 점