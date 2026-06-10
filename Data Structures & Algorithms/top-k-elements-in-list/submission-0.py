from itertools import islice

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}

        # Count occurences of number in array using dictionary
        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1

        # Return top k most occurred elements from array
        dictSorted = sorted(myDict, key=lambda x: myDict[x], reverse=True)

        return dictSorted[:k]
        