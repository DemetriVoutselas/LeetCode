class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1: return False
        Stack = ['']
        for i in s:
            if (i == '(')|(i == '{')|(i == '['):
                Stack.append(i)
            else:
                temp = Stack.pop() + i
                if (temp != '()') & (temp != "{}") & (temp != "[]"):
                     return False
        if len(Stack) == 1: return True
        else: return False
