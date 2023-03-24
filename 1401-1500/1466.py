class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        roads = defaultdict(list)
        for s, d in connections:
            # 1 for outward, 0 for inward
            roads[s].append((d, 1))
            roads[d].append((s, 0))

        def dfs(city, pre_city):
            route_change = 0
            for road in roads[city]:
                if road[0] != pre_city:
                    route_change += dfs(road[0], city)
                    route_change += road[1]
            return route_change
        return dfs(0, -1)
