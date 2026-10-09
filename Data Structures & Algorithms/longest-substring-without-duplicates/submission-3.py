class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #edge cases
        if not s:
            return 0
        
        chars = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            result = max(result, r - l + 1)

        return result