import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
chains = deque(sorted(list(map(int, input().split()))))
ans = 0
while True:
    # 고리의 개수가 작은 체인부터 소모, 하나의 고리는 두 체인을 연결할 수 있음
    chains[0] -= 1
    ans += 1
    last1 = chains.pop()
    last2 = chains.pop()
    chains.append(last1+last2)
    # 0이 되면 해당 체인 모두 소모되었으므로 삭제
    if chains[0] == 0:
        chains.popleft()
    if len(chains) == 1:
        break

print(ans)