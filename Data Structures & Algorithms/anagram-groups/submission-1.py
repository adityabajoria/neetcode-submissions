class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for i, s in enumerate(strs):
            key = ''.join(sorted(s))
            if key in my_dict:
                my_dict[key].append(s)
            else:
                my_dict[key] = [s]
        return list(my_dict.values())