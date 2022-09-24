class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
    # two poiner
        
        max_profit = 0
        
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right += 1
            else:
                diff = prices[right] - prices[left]
                right += 1
                if diff > max_profit:
                    max_profit = diff
        
        return max_profit
                
        
#     # kadane's
#         curr_max = 0
#         max_max = 0
#         for i in range(1, len(prices)):
#             curr_max += prices[i]-prices[i-1]
#             curr_max = max(0, curr_max)
#             max_max = max(curr_max, max_max)
        
#         return max_max