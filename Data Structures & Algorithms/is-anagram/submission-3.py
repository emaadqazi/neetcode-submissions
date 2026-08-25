class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        myDict = {}

        for i in range(len(s)):
            if s[i] not in myDict:
                myDict[s[i]] = 0
            if t[i] not in myDict:
                myDict[t[i]] = 0
            myDict[s[i]] += 1
            myDict[t[i]] -= 1

        for value in myDict.values():
            if value != 0:
                return False 
        
        return True 
