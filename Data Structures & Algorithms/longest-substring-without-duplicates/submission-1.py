class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        mp = {}
        for j in range(len(s)):
            mp[s[j]] = mp.get(s[j], 0) + 1
            while mp[s[j]] > 1:
                mp[s[i]] -= 1
                i += 1

            longest = max(longest, j-i+1)

        return longest       
