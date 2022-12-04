total=0
while True:
    try:
        x = input()
        total += int(x)
        print(x, total)
    except EOFError:
        print("EOF")
        break

print(total)