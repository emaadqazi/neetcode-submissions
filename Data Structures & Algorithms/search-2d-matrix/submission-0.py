class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Each array is sorted from least -> greatest 
        # Need to solve in O(log(m * n)) where m is length of arrays and n is length of numbers in each array?
        
        for i, row in enumerate(matrix):
            if target in row:
                return True 

        return False

            # left = 0
            # right = len(matrix) - 1
            # middle = (left + right) // 2
            # while left <= right:
            #     if target == row[middle]:
            #         return True 
            #     elif target > row[middle]:
            #         left += 1
            #     elif target < row[middle]:
            #         right -= 1