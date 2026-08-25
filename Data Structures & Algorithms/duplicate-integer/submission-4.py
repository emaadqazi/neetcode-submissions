class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        result = set()

        for value in nums:
            if value in result:
                return True
            else:
                result.add(value)

        return False