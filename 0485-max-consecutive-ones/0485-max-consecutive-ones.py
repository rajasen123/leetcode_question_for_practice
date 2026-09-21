class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maximum = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0

            if count > maximum:
                maximum = count

        return maximum