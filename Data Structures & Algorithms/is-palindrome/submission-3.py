class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            s = s.lower()
            if s[left] != s[right] and s[left].isalnum() and s[right].isalnum():
                return False 
            if s[left].isalnum() and s[right].isalnum(): # checks to see one side 
                left += 1
                right -= 1
            elif not s[right].isalnum(): # check to see other side
                right -= 1
            elif not s[left].isalnum(): # check to see other side
                left += 1
            

        return True

    # 7 word: devived
    # 6 word: hallah
