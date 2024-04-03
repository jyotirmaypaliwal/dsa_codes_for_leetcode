class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sbs = []

        def dfs(i):
            if i >= len(nums):
                res.append(sbs.copy())
                return
            
            sbs.append(nums[i])
            dfs(i+1)

            sbs.pop()
            dfs(i+1)

        dfs(0)
        return res