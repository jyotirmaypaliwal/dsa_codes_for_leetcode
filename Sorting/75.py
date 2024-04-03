class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = [0, 0, 0]
        for i in nums:
            if i == 0:
                c[0]+=1
            elif i == 1:
                c[1]+=1
            else:
                c[2]+=1
        d = 0
        for j in c:
            f = 0
            for k in range(j):
                nums[d] = f
                d+=1
            f+=1

