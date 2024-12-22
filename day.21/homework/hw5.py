last_name = input("Enter your last name: ")
response = input("Do you want to convert your last name to uppercase? (yes/no): ")

if response.lower() == "yes":
    print(last_name.upper())
else:
    print(last_name)