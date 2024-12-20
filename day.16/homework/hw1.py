surnames = []
for _ in range(5):
    surname = input("Please enter a surname: ")
    surnames.append(surname)

name = input("Please enter your name: ")

if len(name) > 7:
    surnames.append(name)

print("Updated surnames list:", surnames)