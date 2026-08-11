class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stc = []
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p, s in pair:
            time = (target - p) / s
            if stc and time <= stc[-1]:
                continue
            else:
                stc.append(time)
        return len(stc)