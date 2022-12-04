# make sure to leave an extra blank line at the end of the input file

from sys import stdin

valid = 0
required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional = ["cid"]

cur = {}
new_passport = True

for line in stdin:
    line = line[:-1]
    if new_passport:
        print(cur)
        cur = {}
        new_passport = False
        
    if len(line) > 1:
        entries = line.split(" ")
        for e in entries:
            key, value = e.split(":")
            cur[key] = value
    else:
        new_passport = True

        v = True
        for r in required:
            if r not in cur:
                v = False
                break
        if not v:
            continue

        byr = int(cur["byr"])
        if byr < 1920 or byr > 2002:
            continue

        iyr = int(cur["iyr"])
        if iyr < 2010 or iyr > 2020:
            continue

        eyr = int(cur["eyr"])
        if eyr < 2020 or eyr > 2030:
            continue

        hgt_num = int(cur["hgt"][:-2])
        hgt_unit = cur["hgt"][-2:]
        if hgt_unit == "in":
            if hgt_num < 59 or hgt_num > 76:
                continue
        elif hgt_unit == "cm":
            if hgt_num < 150 or hgt_num > 193:
                continue
        else:
            print("wtf")
            continue

        hcl = cur["hcl"]
        if len(hcl) != 7 or hcl[0] != "#":
            continue
        v = True
        for c in hcl[1:]:
            if c not in list("0123456789abcdef"):
                v = False
                break
        if not v:
            continue

        if cur["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        pid = cur["pid"]
        if len(pid) != 9:
            continue
        pid = int(pid)
        if pid < 0 or pid > 999999999:
            continue

        valid += 1
        print("valid")
        
print(cur)
print(valid)
