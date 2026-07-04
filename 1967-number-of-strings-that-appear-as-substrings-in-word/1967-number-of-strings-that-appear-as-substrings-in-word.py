class Solution(object):
    def numOfStrings(self, patterns, word):
        a=0
        for i in patterns:
            if i in word:
                a+=1
        return a