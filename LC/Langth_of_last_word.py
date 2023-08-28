t = "sfg   "


def lengthOfLastWord(s):
    n = len(s)-1
    if n == 1:
        return 1
    while s[n] == ' ':
        n -= 1
    for i in range(n, -1, -1):
        if s[i] == ' ':
            return (n-i)
        elif i ==0:
            return n+1


answer = lengthOfLastWord(t)
print(answer)
