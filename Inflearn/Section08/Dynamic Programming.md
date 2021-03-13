# Dynamic Programming

> ### 개념

동적 계획법이라고도 하며, 큰 문제를 작은 문제로 나눠서 푸는 알고리즘. Divide and Conquer와 비슷하다. 해결된 문제의 답을 저장하고, 그것을 활용하여 다음 큰 문제를 푸는데 사용한다. 



> ### 사용가능한 조건

1. 최적 부분 구조

   큰 문제를 작은 문제로 나눠 풀 수 있고, 작은 문제의 답을 모아 큰 문제를 해결한다.

2. 동일한 작은 문제를 반복적으로 해결한다.



> ### Memoization

한 번 계산한 결과를 메모리 공간에 메모하는 기법. - Top-down 방식.

같은 문제를 다시 호출하면, 메모했던 결과를 그대로 가져온다.



> ###  Top-down vs. Bottom-up

- Top-down

- Botom-up

  dp의 전형적인 형태. 

  dp 테이블: 결과 저장용 리스트



> ### 피보나치 수열

<img src="https://user-images.githubusercontent.com/68037174/111019538-342c0300-8403-11eb-8523-55180d3a0e77.png" alt="image" style="zoom:50%;" />

- 단순 재귀 - 지수 시간 복잡도

  ```python
  def fibo(x):
      if x == 1 or x == 2:
          return 1
      return fibo(x - 1) + fibo(x - 2)
  
  print(fibo(4))
  ```

  f(2)가 여러번 호출된다.

- 동적 계획법 

  피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족한다.(큰 문제를 작은 문제로 나누고, 작은 문제를 반복적으로 해결한다.)

  - **Top-down**

  ```python
  # 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
  d = [0] * 100
  
  # 피보나치 함수(Fibonacci Function)를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
  def fibo(x):
      # 종료 조건(1 혹은 2일 때 1을 반환)
      if x == 1 or x == 2:
          return 1
      # 이미 계산한 적 있는 문제라면 그대로 반환: cut edge를 한다.
      if d[x] != 0:
          return d[x]
      # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
      d[x] = fibo(x - 1) + fibo(x - 2)
      return d[x]
  
  print(fibo(99))
  ```

  - Bottom-up

  ```python
  # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
  d = [0] * 100
  
  # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
  d[1] = 1
  d[2] = 1
  n = 99
  
  # 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
  for i in range(3, n + 1):
      d[i] = d[i - 1] + d[i - 2]
  
  print(d[n])
  ```

  

> 참고

https://freedeveloper.tistory.com/276