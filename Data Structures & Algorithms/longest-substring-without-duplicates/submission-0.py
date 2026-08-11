from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        window_string = Counter()
        for j in range(0, len(s)):
            window_string[s[j]] += 1
            while window_string[s[j]] > 1:
                window_string[s[i]] -= 1
                i += 1
            longest = max(longest, j-i+1)
        return longest