class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myDict = {}

        for number in nums:
            if number in myDict:
                myDict[number] += 1
            else:
                myDict[number] = 1

        return next(key for key, value in myDict.items() if value == 1)