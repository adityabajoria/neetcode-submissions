class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x) # '111'
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True