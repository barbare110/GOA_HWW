#1
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

for x in list:
    if start <= x <= end:
        print(x)

#2
list = [10, 20, 30, 40, 50]

index = int(input("Enter the index number: "))

if index >= 0 and index < 5:
    print("Element at index", index, "is:", list[index])
else:
    print("Invalid index")

#3
user_name = input("Enter your name: ")
my_name = "Barbara"

result = user_name[:3] + my_name[-2:]

print(result)

#4
# Indexing allows you to get a single element from a list by specifying its index.
# For example, my_list[2] gives you the element at index 2 (the 3rd element).

# Slicing, on the other hand, lets you get a range of elements from a list by specifying a start and end index.
# For example, my_list[1:4] gives you elements from index 1 to 3 (but not 4).

#5
last_name = input("Enter your last name: ")
reversed_last_name = last_name[:-1]

print("Original last name:", last_name)
print("Reversed last name:", reversed_last_name)