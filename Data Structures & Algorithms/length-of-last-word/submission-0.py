class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_arr = s.split() # ['Hello', 'World']
        for i in range(0, len(s_arr)):
            return len(s_arr[-1])