import math

class Solution:
    def computeK(self, piles: List[int], k) -> int:

        total = 0
        for i in piles:
            result = math.ceil(i / k)
            total += result 
        
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # monotonic = consistently non-increasing | consistently non-decreasing 

        # use binary search 
        # if k > h then search right
        # if k < h then search left 

        left = 1
        right = max(piles)
        total = 0

        while left <= right:
            middle = (left + right) // 2
            k = self.computeK(piles, middle)
            if k > h:
                left = middle + 1
            else:
                right = middle - 1

        return left
            


        