class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort()
        profit_heapq = []
        idx = 0

        while k:
            while idx < len(projects):
                if w >= projects[idx][0]:
                    heapq.heappush(profit_heapq, -projects[idx][1])
                    idx += 1
                else:
                    break
            if len(profit_heapq):
                w -= heapq.heappop(profit_heapq)
            else:
                break
            k -= 1

        return w
