class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def possible_to_ship(cap):
            req_days = 1
            cont = 0
            for weight in weights:
                cont += weight
                if cont > cap:
                    req_days += 1
                    cont = weight
            return req_days <= days

        left = max(weights)
        right = sum(weights)
        mid = 0

        while left < right:
            mid = (left + right) // 2
            if possible_to_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left
