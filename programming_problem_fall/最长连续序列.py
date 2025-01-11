class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for i in nums:
            if i - 1 in num_set:
                continue
            y = i + 1
            while y in num_set:
                y += 1
            ans = max(ans, y - i)

        return ans