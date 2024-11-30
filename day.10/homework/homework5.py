number = int(input("Enter a number: "))

for i in range(number, -1, -1):
    if i % 2 == 0:
        print(i)