# Intcode computer
# Takes initial memory, returns final memory
def intcode(memory):
    pointer = 0
    while True:
        if memory[pointer] == 1:
            a, b, c = memory[pointer+1:pointer+4]
            memory[c] = memory[a] + memory[b]
            pointer += 4
        elif memory[pointer] == 2:
            a, b, c = memory[pointer+1:pointer+4]
            memory[c] = memory[a] * memory[b]
            pointer += 4
        elif memory[pointer] == 99:
            break
        else:
            print("Unknown code", memory[pointer], "at position", pointer)
            break
    return(memory)

initial_memory = [int(i) for i in input().split(",")]
final_memory = intcode(initial_memory)
print("Memory contents:", final_memory)
