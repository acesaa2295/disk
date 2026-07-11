class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node, comp):
            visited[node] = True
            comp.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, comp)

        ans = 0

        for i in range(n):
            if not visited[i]:
                comp = []
                dfs(i, comp)

                vertices = len(comp)
                degree_sum = sum(len(graph[v]) for v in comp)
                edge_count = degree_sum // 2

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans