class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p = []
        n = []
        for i in range(len(nums)):
            if nums[i]>0:
                p.append(nums[i])
            else:
                n.append(nums[i])
        result = []
        for i in range(len(nums)//2):
            result.append(p[i])
            result.append(n[i])
        return result
