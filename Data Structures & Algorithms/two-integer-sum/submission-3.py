class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # BRUTE FORCE O(n^2)
        # Iterate over every indice in the array
        # Create another nested loop and iterate from that number to 
        # every other number in the array 
        # Return if there is a match with target

        # HASH MAP (Efficient)
        # Initialize hash map
        # Create one for loop to iterate over nums 
        # Dictionary stores key : index
        # At every #, check for difference needed to get to target
        # If that number is in dictionary, we can retrieve the index
        # alongside the current number and find our answer

        myDict = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in myDict:
                return [myDict[difference], i]
            else:
                myDict[nums[i]] = i

        




        
        