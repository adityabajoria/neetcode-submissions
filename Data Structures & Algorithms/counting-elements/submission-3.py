class Solution:
    def countElements(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            if arr[i] + 1 in arr:
                ans += 1
        return ans