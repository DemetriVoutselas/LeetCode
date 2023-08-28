class Solution:
    def romanToInt(self, s: str) -> int:
        sol = 0
        prev = 'M'
        hash = {'I':1,'V':5,
        'X':10,'L':50,'C':100,
        'D':500,'M':1000}
        for i in s:
            if hash[i] > hash[prev]:
                sol = sol - 2*hash[prev] + hash[i]
            else:
                sol += hash[i]
            prev = i
        return sol

Sol = Solution()
st = input('Roman Numeral: ')
print(Sol.romanToInt(st))