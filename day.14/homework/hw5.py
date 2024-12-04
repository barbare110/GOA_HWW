user_input = input("Enter 10 numbers separated by spaces: ")
numbers = []
for i in range(10):
    number = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(number)

first_three = numbers[:3]
print("First three numbers:", first_three)

middle_four = numbers[3:7]
print("Middle four numbers:", middle_four)

if numbers[-1] == 10:
    print("The last number is 10.")
else:
    print("The last number is not 10.")