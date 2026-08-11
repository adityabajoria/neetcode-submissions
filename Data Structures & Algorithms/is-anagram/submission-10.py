class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s = {}
        mp_t = {}
        for char in s:
            mp_s[char] = mp_s.get(char, 0) + 1
        
        for char in t:
            mp_t[char] = mp_t.get(char, 0) + 1
        
        return True if mp_s == mp_t else False