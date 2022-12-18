s = input()

ups = s.count("(")
downs = s.count(")")
print( ups-downs )

running_total=0
count=0
for i in s:
    count += 1
    running_total = running_total+1 if i=="(" else running_total-1
    if running_total < 0:
        print(count)
        break
