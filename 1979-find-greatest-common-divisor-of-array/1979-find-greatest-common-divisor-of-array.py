class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return find_gcd(min(nums),max(nums))