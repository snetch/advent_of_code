from sys import stdin

valid1 = 0
valid2 = 0

for line in stdin:
    sp1 = line.split(" ")
    min, max = sp1[0].split("-")
    min = int(min)
    max = int(max)
    check = sp1[1][0]
    password = sp1[2]

    if (password[min-1]==check) ^ (password[max-1]==check):
        valid2 += 1

    count=0
    while password.find(check) > -1:
        password = password[ password.find(check)+1: ]
        count += 1
    if count >= min and count <= max:
        valid1 += 1

print(valid1)
print(valid2)
