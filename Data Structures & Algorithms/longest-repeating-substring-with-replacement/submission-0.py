from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        longest = 0
        window = Counter()
        max_freq = 0
        for j in range(0, len(s)):
            window[s[j]] += 1
            max_freq = max(max_freq, window[s[j]])
            while j-i+1 - max_freq > k:
                window[s[i]] -= 1
                i += 1
                max_freq = max(window.values()) if window else 0
            longest = max(longest, j-i+1)
        return longest