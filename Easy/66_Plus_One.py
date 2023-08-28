def plusOne(digits):
    D = len(digits) - 1
    while digits[D] == 9:
        if D == 0:
            digits.insert(0, 0)
            break
        else:
            D -= 1
    digits[D] += 1
    for d in range(len(digits)-1, D, -1):
        print(digits[d])
        digits[d] == 0
    return digits
