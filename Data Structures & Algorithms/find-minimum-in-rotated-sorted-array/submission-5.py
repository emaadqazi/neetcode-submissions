class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # We do not know how many times it has been rotated 
        # There must be some logic to derive it 
        # And then apply BS to move depending on the results 
        # [3, 4, 5, 6, 1, 2] 
        # [4, 5, 0, 1, 2, 3]
        # [4, 5, 6, 7]
        # -> if we compare L and R and L is greater than R, then 

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[right] < nums[middle]:
                left = middle + 1
            elif nums[right] >= nums[middle]: 
                right = middle 

        return nums[left]

            

