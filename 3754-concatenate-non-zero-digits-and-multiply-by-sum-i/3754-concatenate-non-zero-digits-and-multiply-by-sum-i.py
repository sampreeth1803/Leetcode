class Solution(object):
    def sumAndMultiply(self, n):
        s = ''.join(ch for ch in str(n) if ch != '0')
        return int(s) * sum(map(int, s)) if s else 0
        