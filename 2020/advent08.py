from sys import stdin

code = []
for line in stdin:
    op, arg = line[:-1].split(" ")
    code.append( [ op, int(arg) ] )

def attempt(c):
    acc = 0
    inst = 0
    visited = []
    while True:
        if inst >= len(c):
            print("  PROPER TERMINATION #######################################################")
            break

        # pad "visited" if not long enough
        if len(visited) <= inst:
            visited += [False]*(inst - len(visited) + 1)

        if visited[inst]:
            print("  Repeat detected")
            break
        else:
            visited[inst] = True

        if c[inst][0] == "nop":
            inst += 1
        elif c[inst][0] == "acc":
            acc += c[inst][1]
            inst += 1
        elif c[inst][0] == "jmp":
            inst += c[inst][1]
    print("    Instruction:", inst)
    print("    Accumulator value:", acc)

print("Original code:")
attempt(code)

for i in range(len(code)):
    if code[i][0] == "jmp":
        print("Changing jmp to nop at instruction", i)
        code[i][0] = "nop"
        attempt(code)
        code[i][0] = "jmp"
    elif code[i][0] == "nop":
        print("Changing nop to jmp at instruction", i)
        code[i][0] = "jmp"
        attempt(code)
        code[i][0] = "nop"
