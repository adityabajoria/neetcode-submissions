class Solution:
    def nextGreatest(self, arr):
        v = []
        s = []
        for i in range(len(arr)-1, -1, -1):
            while s and arr[s[-1]] <= arr[i]:
                s.pop()
            if not s:
                v.append(-1)
            else:
                v.append(s[-1])
            s.append(i)
        return v[::-1]
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        right = self.nextGreatest(temperatures)
        for i in range(0, len(right)):
            if right[i] == -1:
                ans.append(0)
            else:
                ans.append(right[i]-i)
        return ans