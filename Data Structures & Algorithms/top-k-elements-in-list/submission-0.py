class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] +=1
        print(counter)
        sorted_nums = sorted(counter, key = counter.get, reverse = True)
        print(sorted_nums)
        for i in range(k):
            result.append(sorted_nums[i])
        return result