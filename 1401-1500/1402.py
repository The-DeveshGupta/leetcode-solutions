class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort(reverse=True)
        adder_one, adder_two = 0, 0

        for idx in range(len(satisfaction)):
            adder_two += satisfaction[idx] + adder_one
            adder_one += satisfaction[idx]
            satisfaction[idx] = adder_two

        return max(0, max(satisfaction))
