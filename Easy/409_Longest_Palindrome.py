class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Frequency table
        frq = {}
        for let in s:
            if let in frq:
                frq[let] += 1
            else:
                frq[let] = 1
        count = 0
        odd = 0
        if max(frq.values()) == 1:
            return 1
        if min(frq.values()) == 1:
            odd = 1

        for val in frq.values():
            if val % 2 == 0:
                count += val
            elif val > 2:
                count += val - 1
                odd = 1
        return count + odd
