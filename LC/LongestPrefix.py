class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]
        print(base)
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base

    
sol = Solution()
inp = ["flower","floor","forest","find"]
print(sol.longestCommonPrefix(inp))
