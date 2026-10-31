class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            if nums[m]<target:
                l=m+1
            if nums[m]>target:
                r=m-1
        return l