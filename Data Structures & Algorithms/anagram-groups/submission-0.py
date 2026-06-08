class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Go through arrays 
        # Sort each 
        # Add word to dictionary if match otherwise create new entry

        myDict = {}

        for word in strs:
            temp = ''.join(sorted(word))
            if temp in myDict:
                myDict[temp].append(word)
            else:
                myDict[temp] = [word]

        # We need to return a List[List[str]] - list of list of strings
        return list(myDict.values())