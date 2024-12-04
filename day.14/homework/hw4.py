numbers = list(range(500, 10001, 500))

first_five = numbers[:5]

every_third = numbers[::3]

count = 0
for num in numbers:
    count += 1

print("First five numbers:", first_five)
print("Every third number:", every_third)
print("Total number of elements:", count)