# Demonstrating methods
text = "Hello123455"

# isalnum() checks if all characters are alphanumeric (letters and numbers)
print(text.isalnum())  

# isdigit() checks if the string contains only digits
print("12345".isdigit())  
print("123a45".isdigit())  

# islower() checks if all characters are lowercase
print("hello".islower())  
print("Hello".islower())  

# isnumeric() checks if the string contains only numeric characters
print("123".isnumeric()) 
print("123abc".isnumeric())  

# isupper() checks if all characters are uppercase
print("HELLO".isupper())  
print("Hello".isupper())  

# count() counts occurrences of a substring in the string
print("hello world".count('l'))  