line = " " + input()

block_length = 14  # 4 or 14, depending on puzzle part
current = block_length

print(line)
while current < len(line):
    print("checking", current)
    found = False
    for j in range(1, block_length):
        if line[current-j] in line[current-j+1 : current+1]:
            current += block_length - j
            found = True
            break
    if not found:
        print("found", current)
        break
 