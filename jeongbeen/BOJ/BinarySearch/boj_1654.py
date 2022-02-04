"""
<문제 링크>
https://www.acmicpc.net/problem/1654

<알고리즘>
-기본적인 이진탐색과 달리 역으로 searchNum을 찾아야 하는 상황
-각 수열에서 middle단위가 몇 번 나오는가?
    -전체 개수가 원하는 개수보다 작다면 단위 길이를 줄이기
    -전체 개수가 원하는 개수보다 크면 단위 길이를 늘리기
"""

# 가지고 있는 랜선 수, 만들고 싶은 랜선 수
k,n = map(int, input().split())

# 각 랜선 길이 가지고 있는 리스트
lans = [int(input()) for _ in range(k)]

# 초기 섫정 (index가 아니라 실제 수를 지정한다!)
left, right = 1, max(lans)

### 이진탐색 ###
while left <= right:
    middle = (left + right) // 2  # 역시 index가 아니고 실제 수
    cnt = 0  # 만들 수 있는 랜선 개수

    for lan in lans:
        cnt += lan // middle  # 분할된 랜선 개수

    if cnt < n:  # 랜선을 너무 큼지막하게 자른 경우
        right = middle - 1
    else:  # 랜선을 너무 잘게 자른 경우
        left = middle + 1


print(right)