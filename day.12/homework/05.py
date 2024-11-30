# 6
number = int(input("Enter a number (position): "))
names = ["Nino", "Nara", "George", "Barbara", "Jack"]

count = 0
for name in names:
    if count == number:
        print("The name at position", number, "is:", name)
        break
    count += 1
else:
    print("The number is not a valid position.")

# with index
index = int(input("Enter a number (must be valid index): "))
names = ["Nino", "Nara", "George", "Barbara", "Jack"]

if 0 <= index < len(names):
    print("The name at the index is:", names[index])
else:
    print("The number is not a valid index.")