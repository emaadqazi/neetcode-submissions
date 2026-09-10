class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Iterate over every value 
        # Current val is temp
        # if temp < min : make new min
        # if temp > max : make new max 
        if len(prices) == 0:
            return 0

        low = prices[0] 
        result = 0

        for number in prices:
            if low > number: # if we find lower number, store
                low = number 
            
            # Get profit and keep running total
            profit = number - low 
            result = max(result, profit)

        return result


