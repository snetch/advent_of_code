from sys import stdin

def safe(levels):
    prev = levels[0]
    if levels[1] > levels[0]:

        for l in levels[1:]:
            if l - prev > 0 and l - prev < 4:
                prev = l
            else:
                return(False)

    elif levels[1] < levels[0]:

        for l in levels[1:]:
            if prev - l > 0 and prev - l < 4:
                prev = l
            else:
                return(False)

    else:
        return(False)
    return(True)

safe_lines = 0
dampened_safe_lines = 0
for line in stdin:
    line = [int(i) for i in line[:-1].split()]
    if safe(line):
        safe_lines += 1
        dampened_safe_lines += 1
        print("safe")
    else:
        dampened_safe_current = False
        for i in range( len(line) ):
            dampened_line = line[:i] + line[i+1:]
            if safe(dampened_line):
                dampened_safe_current = True
                dampened_safe_lines += 1
                print("dampened_safe")
                break
        if not dampened_safe_current:
            print("unsafe")

print(safe_lines)
print(dampened_safe_lines)
