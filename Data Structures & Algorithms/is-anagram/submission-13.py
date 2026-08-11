class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp_s = {}
        for x in s:
            mp_s[x] = mp_s.get(x, 0) + 1
        mp_t = {}
        for x in t:
            mp_t[x] = mp_t.get(x, 0) + 1
        
        return mp_s == mp_t