class Solution(object):
    def maxProduct(self, n):
        b=[]
        for a in str(n):
            b.append(int(a))
        b.sort(reverse=True)
        return b[0]*b[1]