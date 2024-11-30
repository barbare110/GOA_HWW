# 1
list = [10, 15, 20, 25, 30, 35, 40, 50, 55,60]

index = int(input("Enter index (0-9): "))

if index >= 0 and index <= 9:
    print("Element at index", index, list[index])
else:
    print("Entered index is invalid.")

# 2
list_names = ["Maria", "Barbara", "George", "David", "Alice"]

user_name = input("enter your name: ")
index = int(input("enter an index (0-4): "))

if index >= 0 and index <= 4:
    list_names [index] = user_name
    print("Updated list:", list_names)
else:
    print("entered index is invalid.")
#3
#Objects that can be changed after creation.Lists. You can modify, add, or remove the elements.
## Immutable: Objects that cannot be changed after creation.Tuples(immutable sequence). 
# Once created, their elements can't be changed.