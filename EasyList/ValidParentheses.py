class Solution:
    def isValid(self, s: str) -> bool:
        simbolMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        if s == '':
            return True
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) > 0 and stack[-1] == simbolMap[char]:
                stack.pop()
            else:
                return False           
        return len(stack) == 0


print(Solution().isValid('(([]))[]{{}}'))