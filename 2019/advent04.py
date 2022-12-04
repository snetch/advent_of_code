MIN = 165432
MAX = 707912

def int_to_list_of_digits(n):
    digits = []
    while n>0:
        digits.insert(0, n%10)
        n //= 10
    return digits

def fits(num):
    x = [15] + int_to_list_of_digits(num) + [15]
    if len(x) != 8:
        return False
    adjacent = False
    for i in range(1,6):
        if x[i] > x[i+1]:
            return False
        elif x[i] == x[i+1]:
            if x[i] != x[i-1] and x[i+1] != x[i+2]:
                adjacent = True
    if not adjacent:
        return False
    return True

fitting_passes = [p for p in range(MIN, MAX+1) if fits(p)]
print(len(fitting_passes))
