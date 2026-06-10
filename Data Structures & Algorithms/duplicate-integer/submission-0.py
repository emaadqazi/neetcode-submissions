class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        myDict = {}

        for number in nums:
            if number in myDict:
                return True 
            else:
                myDict[number] = [1]

        return False

