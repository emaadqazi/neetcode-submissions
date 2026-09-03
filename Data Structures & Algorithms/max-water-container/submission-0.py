class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # How to define the box that the water is going to fit inside?
        # There has to be some pattern we can use
        # We can track the width via indices
        # Track height by the value of the indice 

        left = 0 
        right = len(heights) - 1
        total = 0

        while left <= right:

            maxHeight = min(heights[left], heights[right]) # Get the minimum height of the two 
            maxWidth = right - left 
            maxWater = maxHeight * maxWidth 
            if maxWater > total:
                total = maxWater 

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return total

        # (1)
        # left = 0 (val=2)
        # right = 2 (val=2)
        # while 0 <= 2
        # maxH = min(2, 2) => 2
        # maxW = 2 - 0 = 2
        # maxWater = 2 * 2 => 4
        # total =4
        #
        # (2)
        # left = 1 (val=2)
        # right = 1 (val=2)
        # maxH = min(2, 2) => 4
        # maxW = 1 - 1 => 0
        # maxWater = 4 * 0 => 0
        # if 0 > 4 -> total = 0 but 0 is not > 4
        # left = 2
        # right = 0
        # loop terminates on next run because 2 is not <= 0
        # maxWater should be 4 from iteration 1
         










