class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k 

        def quickSelect(l, r):
            pivot, p = nums[r], l
            while p < r:
                if nums[l] <= pivot:
                    nums[p], nums[l] = nums[l], nums[p]
                    p+=1
                    l+=1
                else:
                    l+=1
            
            nums[p], nums[r] = nums[r], nums[p]
            if k > p:
                return quickSelect(p+1, r)
            elif p == k:
                return nums[p]

            else:
                return quickSelect(l, p-1)

        return quickSelect(0, len(nums)-1)

