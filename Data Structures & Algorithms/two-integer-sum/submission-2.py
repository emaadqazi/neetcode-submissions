class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Iterate over every indice in the array
        # Create another nested loop and iterate from that number to 
        # every other number in the array 
        # Return if there is a match with target

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        