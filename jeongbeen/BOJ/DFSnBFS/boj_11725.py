"""
<문제 링크>
https://www.acmicpc.net/problem/11725

<알고리즘>
- 트리 상에서 연결된 두 정점
    - 인접 리스트에서 서로의 원소 넣기
        e.g.) 1  6 → graph[1].append(6), graph[6].append(1)
- 각 노드의 부모를 표시하는 list를 만들자
    - bfs(1) 호출 시 그의 직계 자손에 대해서 재귀를 하는데,
      다시 말하면 결국 이 직계 자손의 직계 부모는 본인들을 호출한 노드(맥락상 1)이므로 이를 따로 표시하자
"""


from collections import deque

n = int(input())

# 인접 리스트
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


# 최종적으로 [0],[1] 빼고 0이 아닌 양수가 들어가면
# 모두 방문했으면서 부모도 표시한 상태이다.
parent = [0] * (n+1)


def bfs(node):
    # 초기 설정 (root인 1을 최초 방문)
    parent[node] = -1  # 다른 노드의 인접한 노드로 '1'이 나올 경우 다시 방문하는 것을 방지하기 위해 -1을 넣는다.
    queue = deque([node])

    while queue:
        now = queue.popleft()
        for elem in graph[now]:
            if parent[elem] == 0:
                parent[elem] = now
                queue.append(elem)

    return True


bfs(1)

for i in range(2,n+1):
    print(parent[i])