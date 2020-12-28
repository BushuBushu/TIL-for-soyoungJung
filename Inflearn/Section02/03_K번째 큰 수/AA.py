N, K = map(int, input().split())
cnum = list(map(int, input().split()))
#print(cnum)

#3장을 뽑을 수 있는 모든 경우의 수..?!
# range를 N - 1, N - 2, N -3으로 주고, append 시 index를 +로 주는 시나리오는??
l = set()
for f in range(N):
    for s in range(f + 1, N):
        for t in range(s + 1, N):
            l.add(cnum[f] + cnum[s] + cnum[t])

l = list(l)
l.sort(reverse = True)

print(l[K - 1])