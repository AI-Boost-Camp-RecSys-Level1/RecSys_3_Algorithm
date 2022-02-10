"""
<문제 링크>
https://www.acmicpc.net/problem/2805
<알고리즘>
- (1,나무 높이 중 최댓값)을 범위로 이진탐색 진행
- 각 나무 높이 - middle : 가져가게 되는 나무
    - 0 이하이면 가져가는 것 없음.
"""


# 나무의 수, 가져가려는 나무의 길이
n, m = map(int,input().split())

# 주어진 나무들 높이
trees = list(map(int,input().split()))

left, right = 1, max(trees)

while left <= right:
    middle = (left + right) // 2

    result = 0  # 가져갈 나무 길이
    for tree in trees:
        temp = tree - middle
        if temp > 0:
            result += temp


    if result < m:
        right = middle - 1
    else:
        left = middle + 1

print(right)