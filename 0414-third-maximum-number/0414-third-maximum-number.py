class Solution(object):
    def thirdMax(self, nums):
        v = sorted(set(nums), reverse=True)
        return v[2] if len(v) >= 3 else v[0]
            