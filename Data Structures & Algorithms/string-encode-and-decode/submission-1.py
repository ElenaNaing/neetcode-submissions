class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        decoded = []
        base_index = 0
        next_delimiter = s.find('#')
        while next_delimiter > -1:
            length = int(s[base_index:next_delimiter])
            decoded.append(s[next_delimiter+1: next_delimiter+1+length])
            base_index = next_delimiter+1+length
            next_delimiter = s[base_index:].find('#')
            if next_delimiter > -1:
                next_delimiter += base_index
        return decoded


