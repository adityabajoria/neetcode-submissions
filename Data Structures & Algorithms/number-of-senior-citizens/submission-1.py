class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_passengers = 0
        for detail in details:
            get_ages = detail[-4: -2]
            ages = int(get_ages)
            if ages > 60:
                count_passengers += 1
        return count_passengers