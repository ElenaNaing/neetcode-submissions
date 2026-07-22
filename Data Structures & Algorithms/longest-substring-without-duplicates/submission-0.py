class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] in mapper:
                left =max(mapper[s[right]]+1,left)
            mapper[s[right]] = right
            result = max(result, right-left +1)
        return result