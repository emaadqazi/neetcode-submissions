class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            elif target == nums[middle]:
                return middle

        return -1

        # [-1, 0, 2, 4, 6, 8]
        # target = 4 (index 3)
        # left = index 0 (val = -1)
        # right = index 5 (val = 8)
        # Iteration 1
        # middle = 0 + 5 => 5 // 2 => 3
        # Index 3 -> val = 2
        # target > nums[middle] = 4 > 2
        # [-1, 0, 2, 4, 6, 8] -> [2, 4, 6, 8]
        # so left = middle -> middle = index 3; left = 3
        # Iteration 2
        # left = 3, right = 5 => middle = 3 + 8 // 2 => 4
        # index 4 in [2, 4, 6, 8] = 