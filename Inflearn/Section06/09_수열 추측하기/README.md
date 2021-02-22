# 문제번호. 문제제목

## 문제 내용


| 난이도 | 정답률(\_%) |
| :----: | :---------: |
|        |             |

## 설계(풀이 방식)

1. 1부터 n까지의 숫자로 만들 수 있는 순열을 모두 구해야 함.
> 1, 2, 3, 4로 만들 수 있는 순열을 모두 만든다. (tree를 만들어 가면서)
```
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                //각 배열의 인덱스끼리 곱한다.
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0
```
2. 1에서 구한 순열을 곱할 이항계수 배열을 구하고 곱한 값을 저장한다.
*** 이항계수 배열을 구하는 이유: 하나의 순열에서 문제와 같은 방법으로 합을 구하는 것은 파스칼의 삼각형 특징과 같음. 
3. 2에서 저장한 값이 구하려는 합과 같다면, 시스템을 종료한다.

## 강의 해설

## 배운 개념 및 깨달은 점
> ### 순열과 조합
- 순열(Permutation): 순서 상관있음.
길이가 n인 배열에서 r개의 요소를 차례로 뽑아 새로운 배열을 만들 때, 가능한 모든 배열의 갯수.
    - 공식

    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FIZiip%2FbtqHxcMFpBH%2FIXkY0zhbCpdDUupwGIaFl1%2Fimg.png)

- 조합(Combination): 순서 상관 없음.
순서가 중요하지 않은 순열.
    - 공식

    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1VoaF%2FbtqHwhuc6V1%2FeddeOid2XphAQ1W3PVZF0K%2Fimg.png)
    
    순열에서 "순서를 결정하는 수"인 `r!`만큼을 나눠줘야 함.

- 이항 정리
(a+b)의 n승을 전개한 것
    - 공식

    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F1VoaF%2FbtqHwhuc6V1%2FeddeOid2XphAQ1W3PVZF0K%2Fimg.png)
    
    *** 이항계수를 사용할 수 있다.

- 파스칼의 삼각형
파스칼의 삼각형(Pascal's triangle)은 수학에서 이항계수를 삼각형 모양의 기하학적 형태로 배열한 것
![](https://www.ebsmath.co.kr/innovativelrms/web_lrms/upload/editor/1550556793204.bmp)


## 정리

| 내 코드 (ms) | 빠른 코드 (ms) |
| :----------: | :------------: |
|              |                |

## 고생한 점