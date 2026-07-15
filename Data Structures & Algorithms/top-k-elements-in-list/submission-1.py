class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frq = defaultdict(int)
        for num in nums:
            frq[num] +=1
        sorted_nums = sorted(frq, key = frq.get, reverse= True)
        for i in range(k):
            result.append(sorted_nums[i])
        return result