def firstlast(numberline):
    digitsonly = [c for c in numberline if c.isdigit()]
    return( int(digitsonly[0]) * 10 + int(digitsonly[-1]))

# zero never happens, just a placeholder
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum1 = 0
sum2 = 0
while True:
    try:
        line = input()

        # comment out next line for part 2 example because that one sometimes doesn't have enough normal digits
        sum1 += firstlast(line)

        lefts = [line.find(d) for d in digits ]
        lefts = [i if i>-1 else len(line)  for i in lefts]
        rights = [line.rfind(d) for d in digits]

        lefts_min_index = lefts.index( min(lefts) )
        rights_max_index = rights.index( max(rights) )

        if max(rights) > -1:
            line = line[:max(rights)] + str(rights_max_index) + line[max(rights):]
        if min(lefts) < len(line) and min(lefts) != max(rights):
            line = line[:min(lefts)] + str(lefts_min_index) + line[min(lefts):]

#        print(line)
        sum2 += firstlast(line)

    except EOFError:
        print("EOF")
        print(sum1)
        print(sum2)
        break
