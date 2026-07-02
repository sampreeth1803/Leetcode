class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, c, ans = len(a)-1, len(b)-1, 0, []
        while i >= 0 or j >= 0 or c:
            c += (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            ans.append(str(c & 1))
            c >>= 1
            i, j = i - 1, j - 1
        return ''.join(ans[::-1])