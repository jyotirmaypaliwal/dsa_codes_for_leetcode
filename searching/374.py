# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            m = (low+high)//2
            if isBadVersion(m) == False:
                if isBadVersion(m+1):
                    return m+1
                else:
                    low = m+1 
            elif isBadVersion(m) == True:
                if isBadVersion(m-1):
                    high = m-1 
                else:
                    return m 

            