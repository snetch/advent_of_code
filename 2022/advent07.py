dirs = {}
current_path = []

while True:
    line = input()
#    print(line)
    # make sure to have a blank line at the end of the input
    if line == "":
        break

    command = line.split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "/":
                current_path = []
            elif command[2] == "..":
                current_path = current_path[:-1]
            else:
                current_path.append(command[2])
#            print("entered", current_path)
        elif command[1] == "ls":
#            print("ls path", current_path)

            # the little block that gives you current_dir initialized as a reference inside dirs
            current_dir = dirs
            for i in current_path:
                current_dir = current_dir[i]

            # initialize the counts for the next big else block
            current_dir["filesize"] = 0
            current_dir["files"] = []
    else:
        if command[0] == "dir":
            current_dir[command[1]] = {}
        else:
            # thankfully no directory in all of input is named "filesize" or "files"
            current_dir["filesize"] += int(command[0])
            current_dir["files"].append(command[1])

#print(dirs)

n = 0
minimum_dir = 70000000  # not needed for the first run, but setting so that they exist
space_needed = 70000000  # same as above

def walk(structure, name):
    global n
    global minimum_dir
    global space_needed
    total_size = 0
    for i in structure:
        if i == "filesize":
            total_size += structure[i]
        elif i != "files":
            total_size += walk(structure[i], name+i+"/")
#    print("total size of", name, ":", total_size)
    if total_size <= 100000:
        n += total_size
    if total_size <= minimum_dir and total_size >= space_needed:
        minimum_dir = total_size
    return(total_size)

space_used = walk(dirs, "/")
print(n)

space_needed = space_used - 40000000
minimum_dir = 70000000
walk(dirs, "/")
print(minimum_dir)
