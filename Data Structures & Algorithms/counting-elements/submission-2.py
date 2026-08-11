class Solution:
    def countElements(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            if arr[i] + 1 in arr:
                ans += 1
        return ans