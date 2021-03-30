n = int(input())
m = list(map(int, input().split()))
m.sort()

print(m[0] * m[-1])

#강의 풀이
#입력의 최대값과 최솟값을 곱하기
#시간복잡도 O(M)