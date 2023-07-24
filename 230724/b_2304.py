import sys
input = sys.stdin.readline

n = int(input())
bar = [0 for _ in range(1001)]          # 최대 1000개의 기둥이 존재하므로 MAX_VALUE는 1000
mIdx = 0        # 가장 큰 기동의 인덱스
mHeight = 0     # 가장 큰 기둥의 높이
for i in range(n):
    x, h = map(int, input().split())
    bar[x] = h
    if h > mHeight:
        mHeight = h
        mIdx = x

# 왼쪽 탐색
# 현재 기둥 보다 높은 기둥이 나오면 기둥 높이 갱신
# 그렇지 않으면 현재 기둥만큼 계속 더함.
cur = 0
total = 0
for i in range(mIdx+1):
    cur = max(cur, bar[i])
    total += cur

# 오른쪽 탐색 (맨 마지막 부터 가장 높은 기둥까지 내림 차순)
# 현재 기둥 보다 높은 기둥이 나오면 기둥 높이 갱신
# 그렇지 않으면 현재 기둥만큼 계속 더함.
cur = 0
for i in range(1000, mIdx, -1):
    cur = max(cur, bar[i])
    total += cur

print(total)


