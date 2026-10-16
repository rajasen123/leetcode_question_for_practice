class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashset = set(nums)
        largest = 0
        for x in hashset:
            if x-1 not in hashset:
                count = 1
                current = x
                while current+1 in hashset:
                    count = count + 1
                    current = current +1
                largest = max(largest , count)
        return largest