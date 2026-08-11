from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        window_s = Counter(s)
        window_t = Counter(t)
        return True if window_s == window_t else False