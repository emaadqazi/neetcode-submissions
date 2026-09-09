class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            middle = (top + bottom) // 2
            if target > matrix[middle][-1]: # this returns last value in the highest row
                top = middle + 1
            elif target < matrix[middle][0]: # this returns shorest value in the row
                bottom = middle - 1
            else: # we found the row and need to extit the loop
                break

        if not top <= bottom: # if we violate this condition then we've searched every row and not found target
            return False

        row = (top + bottom) // 2
        left = 0
        right = cols - 1

        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True 
        return False
            
