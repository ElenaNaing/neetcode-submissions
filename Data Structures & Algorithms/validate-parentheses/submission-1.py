class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closes_to_open = {')':'(','}':'{',']':'['}
        for c in s:
            if c in closes_to_open:
                if stack and stack[-1] == closes_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False