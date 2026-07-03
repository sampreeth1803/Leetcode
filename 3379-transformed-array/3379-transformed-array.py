class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = [0] * n
        for i in range(n):
            landing_index = (i + nums[i]) % n
            result[i] = nums[landing_index]
        return result
        