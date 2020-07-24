class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_numbers = 0        

        for i in range(len(s) - 1):
            if romanDict[s[i]] < romanDict[s[i+1]]:
                sum_numbers -= romanDict[s[i]]
            else:
                sum_numbers += romanDict[s[i]]
        sum_numbers += romanDict[s[-1]]
        return sum_numbers

sol = Solution()
print(sol.romanToInt('IV'))