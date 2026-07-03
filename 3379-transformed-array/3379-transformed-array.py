class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = list(nums)
        for i in range(n):
            if nums[i]==0:
                result[i]=0
            if nums[i]>0:
                result[i]=nums[(i+nums[i])%n]
            if nums[i]<0:
                result[i]=nums[(n+(i+nums[i]))%n]
        return result
        