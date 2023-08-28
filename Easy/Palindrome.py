class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

sol = Solution()
Num = input("Enter Number ")
print(sol.isPalindrome(Num))