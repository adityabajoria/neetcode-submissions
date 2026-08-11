from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s1) > len(s2):
            return False
        s1_window = Counter(s1)
        s2_window = Counter(s2[:k])

        if s1_window == s2_window:
            return True

        for i in range(0, len(s2)-k):
            prev_digit = s2[i]
            s2_window[prev_digit] -= 1
            leading_digit = s2[i+k]
            s2_window[leading_digit] += 1
            if s1_window == s2_window:
                return True
        return False
