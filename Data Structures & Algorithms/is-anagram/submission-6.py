class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        
        dict_t = {}
        for char in t:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1
        
        if dict_s == dict_t:
            return True
        else:
            return False