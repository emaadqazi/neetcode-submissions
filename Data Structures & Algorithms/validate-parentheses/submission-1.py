class Solution:
    def isValid(self, s: str) -> bool:

        # Then think about how the current closing bracket could be compared against 
        # the most recently opened bracket.

        myDict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            if char in myDict:
                if stack and stack[-1] == myDict[char]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)

        return True if not stack else False



        
        