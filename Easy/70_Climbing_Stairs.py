import math


class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if n % 2 == 0:
            m = n//2
            for i in range(m+1):
                count += math.factorial(m+i) / \
                    (math.factorial(m-i)*math.factorial(2*i))

        else:
            m = n//2 + 1
            for i in range(m):
                count += math.factorial(m+i) / \
                    (math.factorial(m-1-i)*math.factorial(2*i+1))
        return int(count)
