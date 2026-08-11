class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            current_score = left.count("0") + right.count("1")
            max_score = max(max_score, current_score)
        return max_score