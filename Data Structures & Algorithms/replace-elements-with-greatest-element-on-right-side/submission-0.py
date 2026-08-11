class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(arr)):
            max_r = -1
            for j in range(i+1, len(arr)):
                if arr[j] > max_r:
                    max_r = arr[j]
            ans.append(max_r)
        return ans
