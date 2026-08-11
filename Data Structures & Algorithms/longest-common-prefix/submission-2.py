class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first_element = strs[0]
        for i in range(len(first_element)):
            for s in strs:
                if i == len(s) or s[i] != first_element[i]:
                    return res
            res += first_element[i]
        return res