from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        window_s = Counter(s)
        window_t = Counter(t)
        if window_s == window_t:
            return True
        return False