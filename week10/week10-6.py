class Solution:
    def average(self, salary: List[int]) -> float:
        s=salary
        return (sum(s)-max(s)-min(s))/(len(s)-2)#扣掉最大值和最小值，數目因扣掉最大和最小值所以要-2