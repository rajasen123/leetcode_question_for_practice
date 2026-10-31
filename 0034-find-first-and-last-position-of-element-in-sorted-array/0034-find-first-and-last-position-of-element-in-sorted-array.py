class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def bound(nums, x, type):
            l, r = 0, len(nums)-1
            ans = len(nums)

            while l <= r:
                m = (l+r)//2

                if (type == "lower" and nums[m] >= x) or (type == "upper" and nums[m] > x):
                    ans = m
                    r = m-1
                else:
                    l = m+1

            return ans

        ans = [bound(nums, target, "lower"), bound(nums, target, "upper")-1]

        if ans[0] == len(nums) or nums[ans[0]] != target:
            return [-1, -1]

        return ans