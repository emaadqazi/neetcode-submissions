class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        seen = {}
        maxVal = 0
        result = 0


        for right in range(len(s)):
            # if s[right] not in seen:
            #     seen[s[right]] = 1
            # else:
            #     seen[s[right]] += 1
            seen[s[right]] = seen.get(s[right], 0) + 1 # one liner for the above 
            maxVal = max(maxVal, seen[s[right]]) # get the max occurence

            while (right - left + 1) - maxVal > k: # move window while it denies result
                seen[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1) # track max distance for valid windows

        return result

        