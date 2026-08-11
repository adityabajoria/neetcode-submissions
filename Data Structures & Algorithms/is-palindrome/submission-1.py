class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(cleaned) - 1
        while i <= j:
            if cleaned[i] != cleaned[j]:
                return False
            i += 1
            j -= 1
        return True