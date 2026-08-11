class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        for i, val in enumerate(s):
            if val in dict_s:
                dict_s[val] += 1
            else:
                dict_s[val] = 1
        
        dict_t = {}
        for i, val in enumerate(t):
            if val in dict_t:
                dict_t[val] += 1
            else:
                dict_t[val] = 1
        
        if dict_s == dict_t:
            return True
        return False