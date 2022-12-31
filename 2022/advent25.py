from sys import stdin


def snafu_to_decimal(s):
    snafu = s
    place = 1
    dec = 0

    while len(snafu) > 0:
        digit = snafu[-1]
        if digit == "=":
            digit = -2
        elif digit == "-":
            digit = -1
        else:
            digit = int(digit)

        dec += digit * place
        place *= 5
        snafu = snafu[:-1]

    return(dec)


def decimal_to_snafu(d):
    dec = d
    snafu = ""

    while dec > 0:
        rem = dec%5
        dec //= 5
        if rem == 3:
            snafu = "=" + snafu
            dec += 1
        elif rem == 4:
            snafu = "-" + snafu
            dec += 1
        else:
            snafu = str(rem) + snafu

    return(snafu)


sum = 0

for line in stdin:
    line = line[:-1]
    sum += snafu_to_decimal(line)

snafu_sum = decimal_to_snafu(sum)
print(snafu_sum)
