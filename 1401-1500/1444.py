class Solution:

    dp = {}

    def ways(self, pizza: List[str], k: int) -> int:

        key = "#".join(pizza) + "$" + str(k)
        if key in self.dp.keys():
            return self.dp[key]

        if 'A' not in "".join(pizza):
            return 0
        if k in [0, 1]:
            return 1

        n_ways = 0

        for i in range(1, len(pizza)):
            n_ways += self.ways(pizza[:i], 0) * self.ways(pizza[i:], k-1)
        for j in range(1, len(pizza[0])):
            n_ways += self.ways([piece[:j] for piece in pizza], 0) * self.ways([piece[j:] for piece in pizza], k-1)

        self.dp[key] = n_ways % 1000000007
        return n_ways % 1000000007
