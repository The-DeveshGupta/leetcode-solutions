class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        route = defaultdict(list)
        for edge in edges:
            route[edge[0]].append(edge[1])
            route[edge[1]].append(edge[0])

        visited = [0] * n
        clusters = []

        def dfs(node, prev_node=-1):
            if visited[node]:
                return 0
            visited[node] = 1
            new_connections = 0
            for next_node in route[node]:
                if next_node != prev_node:
                    new_connections += dfs(next_node, node)
            return new_connections + 1

        for node in range(n):
            n_nodes = dfs(node)
            if n_nodes: clusters.append(n_nodes)

        return (sum(clusters) ** 2 - sum(cluster ** 2 for cluster in clusters)) // 2
