# Algorithm is done in O(n) time. Where n is length of the longer binary digit and m is length of the shorter binary
# uses "two finger" trick
class Solution:
    def addBinary(self, a, b):
        a_n = len(a)
        a_tick = a_n - 1
        b_n = len(b)
        b_tick = b_n - 1
        answer = ''
        carry = 0
        while (a_tick >= 0) and (b_tick >= 0):
            if (a[a_tick] == '1') and (b[b_tick] == '1'):
                if carry == 0:
                    answer = '0' + answer
                    carry = 1
                else:
                    answer = '1' + answer
                a_tick -= 1
                b_tick -= 1
            elif ((a[a_tick] == '0') and (b[b_tick] == '1')) or ((a[a_tick] == '1') and (b[b_tick] == '0')):
                if carry == 0:
                    answer = '1' + answer
                else:
                    answer = '0' + answer
                    carry = 1
                a_tick -= 1
                b_tick -= 1
            else:
                if carry == 1:
                    answer = '1' + answer
                else:
                    answer = '0' + answer
                a_tick -= 1
                b_tick -= 1

        if (b_tick < 0) and (a_tick >= 0):
            for t in range(a_tick, -1, -1):
                if a[t] == '1':
                    if carry == 1:
                        answer = '0' + answer
                    else:
                        answer = a[:t+1] + answer
                        return answer
                if a[t] == '0':
                    if carry == 1:
                        answer = '1' + answer
                        return a[:t] + answer
                    else:
                        return a[:t+1] + answer

        elif (a_tick < 0) and (b_tick >= 0):
            for t in range(b_tick, -1, -1):
                if b[t] == '1':
                    if carry == 1:
                        answer = '0' + answer
                    else:
                        answer = b[:t+1] + answer
                        return answer
                if b[t] == '0':
                    if carry == 1:
                        answer = '1' + answer
                        return b[:t] + answer
                    else:
                        return b[:t+1] + answer

        if carry == 1:
            answer = '1' + answer
        return answer
