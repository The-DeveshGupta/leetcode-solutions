class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        dp = [0] * (len(jobs) + 1)

        for i, (end, start, profit) in enumerate(jobs):
            j = bisect_right(jobs, start, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[j] + profit)

        return dp[-1]
