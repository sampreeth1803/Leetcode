class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        # Find the index of the first character that completes the set of unique letters
        # by scanning for when a character's total count drops to 0
        smallest_char_index = 0
        counts = {c: s.count(c) for c in set(s)}

        for i, char in enumerate(s):
            if char < s[smallest_char_index]:
                smallest_char_index = i
            counts[char] -= 1
            if counts[char] == 0:
                break

        # Pick the smallest valid character found, remove it, and recurse on the suffix
        picked_char = s[smallest_char_index]
        suffix = s[smallest_char_index + 1 :].replace(picked_char, "")

        return picked_char + self.smallestSubsequence(suffix)

