"""
<문제 링크>
https://programmers.co.kr/learn/courses/30/lessons/43238

<알고리즘>
- 이진탐색으로 푸는 이유?
    - parametric search
        - 최적화 문제 → 결정 문제(Yes/No)
        - 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 문제를 풀 때, 
          탐색 범위를 좁혀가며 각 범위 내에서 조건 만족 여부를 확인하는 방식으로 값을 찾는다.
- (예제 기준) 최대시간 6*10=10분
    - [1,60] 범위로 이진탐색 진행
- middle이라는 숫자까지 7의 배수 개수, 10의 배수 개수?
    - middle = 30, 7의 배수 = [7,14,21,28], 10의 배수 = [10,20,30]
    - 7 혹은 10의 배수 : 7개
"""

def solution(n, times):
    left, right = 1, n*max(times)

    while left <= right:
        middle = (left + right) // 2

        cnt = 0
        for elem in times:
            cnt += middle // elem

        if n <= cnt:
            right = middle - 1
        else:
            left = middle + 1

    return left


print(solution(6,[7,10]))