class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        longest = 0

        for num in numSet:
            if num - 1 not in numSet: # don't waste time if there isn't a previous 
                length = 1
                while num + length in numSet: # this is the while condition I could not figure out
                    length += 1

                longest = max(longest, length) # running total

        return longest