class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        # [1, 2, 2, 3, 4]
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i +1]:
                return True
        
        return False