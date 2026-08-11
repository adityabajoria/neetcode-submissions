class Solution:
    def nextLargerElement(self, arr):
        v = []
        s = []
        for i in range(len(arr)-1, -1, -1):
            while len(s) > 0 and arr[s[-1]] <= arr[i]:
                s.pop()
            if not s:
                v.append(-1)
            else:
                v.append(s[-1])
            s.append(i)
        return v[::-1]

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        right = self.nextLargerElement(temperatures)
        ans = []
        for i in range(len(right)):
            if right[i] == -1:
                ans.append(0)
            else:
                ans.append(right[i]-i)
        return ans