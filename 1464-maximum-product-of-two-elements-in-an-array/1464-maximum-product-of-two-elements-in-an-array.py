class Solution(object):
    def maxProduct(self, nums):
        nums.sort(reverse=True)
        a=nums[0]
        b=nums[1]
        return (a-1)*(b-1)