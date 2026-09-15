class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
            # We need to figure out a way to combine the lists without actually combining them (for TC reasons)
            # And then search the two median values; if odd then return num otherwise add and return 

            # We can start with brute force 

            finalList = []

            while nums1 and nums2:
                if nums1[0] < nums2[0]:
                    finalList.append(nums1.pop(0))
                else:
                    finalList.append(nums2.pop(0))

            while nums1:
                finalList.append(nums1.pop(0))

            while nums2:
                finalList.append(nums2.pop(0))

            length = len(finalList)
            if length % 2 == 0: # even
                middle = length // 2
                return ((finalList[middle - 1] + finalList[middle]) / 2)
            else:
                middle = length // 2
                return finalList[middle]

            