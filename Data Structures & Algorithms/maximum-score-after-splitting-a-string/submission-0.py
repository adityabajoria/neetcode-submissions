class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            left_side = s[:i]
            right_side = s[i:]
            current_score = left_side.count("0") + right_side.count("1")
            max_score = max(max_score, current_score)
        return max_score
            


