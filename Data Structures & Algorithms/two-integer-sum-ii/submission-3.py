class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n-1
        while i <= j:
            total_s = numbers[i] + numbers[j]
            if total_s > target:
                j -= 1
            elif total_s < target:
                i += 1
            else:
                return [i+1, j+1]
        