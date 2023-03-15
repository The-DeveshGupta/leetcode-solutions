class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower_price = float('inf')
        upper_price = 0
        max_profit = 0
        for price in prices:
            if price < lower_price:
                max_profit = max(max_profit, upper_price - lower_price)
                lower_price = price
                upper_price = 0
            else:
                upper_price = max(upper_price, price)
        return max(max_profit, upper_price - lower_price)
    