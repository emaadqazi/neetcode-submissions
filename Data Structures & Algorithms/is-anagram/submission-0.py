class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Create dictionary 
        # Map each 

        if len(s) != len(t):
            return False

        myDict1 = {}
        myDict2 = {}

        for letter in s:
            if letter in myDict1:
                myDict1[letter] += 1
            else:
                myDict1[letter] = 1

        for letter in t:
            if letter in myDict2:
                myDict2[letter] += 1
            else:
                myDict2[letter] = 1

        if myDict1 == myDict2:
            return True
        else:
            return False

        