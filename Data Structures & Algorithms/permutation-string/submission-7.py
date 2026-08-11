from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        s1_window = Counter(s1)
        s2_window = Counter(s2[:k])

        if s1_window == s2_window:
            return True
        
        for j in range(0, len(s2)-k):
            trailing_digit = s2[j]
            leading_digit = s2[j+k]
            s2_window[trailing_digit] -= 1
            s2_window[leading_digit] += 1
            if s2_window == s1_window:
                return True
        return False