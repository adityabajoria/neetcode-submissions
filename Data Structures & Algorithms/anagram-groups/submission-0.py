class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        my_dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(s)
        return list(my_dict.values())