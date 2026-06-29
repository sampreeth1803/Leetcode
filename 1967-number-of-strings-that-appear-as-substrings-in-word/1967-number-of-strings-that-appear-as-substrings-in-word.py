import re
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        pattern=r'[a-z]'
        count=0
        for pattern in patterns:
            if re.search(pattern,word):
                count+=1
        return count