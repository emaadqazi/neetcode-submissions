class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # While stack exists and current is > top of stack 
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop() # remove the top of stack 
                res[prev] = i - prev
            stack.append(i)
        return res
            





                




