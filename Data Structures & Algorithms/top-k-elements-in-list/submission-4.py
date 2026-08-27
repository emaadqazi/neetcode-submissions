class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Initialize dictionary
        # Iterate over nums
        # Store {value : count} in dictionary
        # Create 2D list based on len nums
        # Every index of our list is going to represent the frequency
        # And we need to add numbers based on their frequency
        # Ex: [1, 1, 1, 2, 3, 100] -> we are creating array 2D array with
        # 6 elements
        # index 1 = [2, 3, 100], index 2 = [1]
        # And then return the top k by going backwards 
        # Iterate over the list starting at the end (since its sorted) and decrement
        # Return when count == k

        myDict = {}

        # Dictionary gives us {value : frequency}
        for value in nums:
            if value in myDict:
                myDict[value] += 1
            else:
                myDict[value] = 1
        
        bucket = [[] for _ in range (len(nums) + 1)]

        for key, frequency in myDict.items():
            bucket[frequency].append(key)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
