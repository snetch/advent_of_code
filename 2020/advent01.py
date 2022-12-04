from sys import stdin

seek_sum=2020

expenses=[]
for line in stdin:
    expenses.append(int(line))
expenses.sort()

left=0
right=len(expenses)-1

while left<right:
    current_sum = expenses[left]+expenses[right]
    if current_sum < seek_sum:
        left += 1
    elif current_sum > seek_sum:
        right -= 1
    else:
        print(expenses[left]*expenses[right])
        break

for i in range(0, len(expenses)):
    for j in range(i+1, len(expenses)):
        for k in range(j+1, len(expenses)):
            if expenses[i]+expenses[j]+expenses[k] == seek_sum:
                print(expenses[i], expenses[j], expenses[k], expenses[i]*expenses[j]*expenses[k])
