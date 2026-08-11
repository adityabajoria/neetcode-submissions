class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        longest = 0
        i = 0
        mp = {}
        for j in range(len(fruits)):
            if fruits[j] not in mp:
                mp[fruits[j]] = 1
            else:
                mp[fruits[j]] += 1
            
            while len(mp) > 2:
                mp[fruits[i]] -= 1
                if mp[fruits[i]] == 0:
                    del mp[fruits[i]]
                i += 1
            
            longest = max(longest, j - i + 1)
        return longest