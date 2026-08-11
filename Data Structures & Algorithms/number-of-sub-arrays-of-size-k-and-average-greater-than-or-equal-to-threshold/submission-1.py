class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count_subarrays = 0
        window_sum = sum(arr[:k])
        if window_sum / k >= threshold:
            count_subarrays += 1
        
        for i in range(k, len(arr)):
            trailing_digit = arr[i-k]
            leading_digit = arr[i]
            window_sum -= trailing_digit
            window_sum += leading_digit
            if window_sum / k >= threshold:
                count_subarrays += 1
        return count_subarrays