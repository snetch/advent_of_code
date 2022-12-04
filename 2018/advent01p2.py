all_inputs = []
total = 0
repeated = {0}
success = False

while True:
    try:
        x = int(input())
        all_inputs.append(x)
        total += x
        if total in repeated:
            print("First repeated total:", total)
            success = True
            break
        else:
            repeated.add(total)
    except EOFError:
        print("EOF")
        break

while not success:
    for x in all_inputs:
        total += x
        if total in repeated:
            print("First repeated total:", total)
            success = True
            break
        else:
            repeated.add(total)
