class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Initialize dictionary
        # Iterate over every word in strs
        # 

        myDict = {}

        for word in strs:
            temp = tuple(sorted(word))
            if temp in myDict:
                myDict[temp].append(word)
            else:
                myDict[temp] = [word]

        return list(myDict.values())