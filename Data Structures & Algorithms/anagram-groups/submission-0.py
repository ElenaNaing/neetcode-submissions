class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for strr in strs:
            counter = [0] * 26
            for s in strr:
                counter[ord(s)- ord('a')] += 1
            result[tuple(counter)].append(strr)
        return list(result.values())