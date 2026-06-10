class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        array = sorted(nums)

        for number in range(0, len(array) - 1):
            if array[number] == array[number+1]:
                return True

        return False

