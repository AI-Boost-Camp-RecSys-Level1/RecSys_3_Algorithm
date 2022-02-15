"""
<문제링크>
https://www.acmicpc.net/problem/10844

<알고리즘>
- dp : 2차원의 DP table
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 ...,
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
- (n+1) rows, 10 columns
- 각 줄(row)이 자리수를 의미함. (row=1 → 한 자리수)
- 특정 row에 대한 column들은 해당 숫자가 올 수 있는 경우의 수를 의미함.
e.g.) dp[2][3] = 2 : 두자리 수 중에서 맨 뒤에 3이 올 수 있는 계단 수는 2개임. (23, 43)
- 점화식 : d[r][c] = d[r-1][c-1] + d[r-1][c+1] (단, 1<=c<=8)
          d[r][c] = d[r-1][c-1] (단, c=9)
          d[r][c] = d[r-1][c+1] (단, c=0)
"""
n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

for c in range(1,10):
    dp[1][c] = 1

for r in range(2,n+1):
    for c in range(10):
        if c == 0:
            dp[r][c] = dp[r-1][c+1]
        elif c == 9:
            dp[r][c] = dp[r-1][c-1]
        else:
            dp[r][c] = dp[r-1][c-1] + dp[r-1][c+1]

print(sum(dp[n]) % 1000000000)