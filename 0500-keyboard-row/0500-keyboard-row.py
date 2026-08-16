class Solution(object):
    def findWords(self, words):
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            w_set = set(word.lower())
            if w_set <= row1 or w_set <= row2 or w_set <= row3:
                res.append(word)
        return res