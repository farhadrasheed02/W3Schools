var = "Farhad"
print(len(var))
print(var.upper())
print(var.lower())

var1 = "Farhad rashid !!!!!"
print(var1.rstrip("!"))

print(var1.split(" ")) # splits the string into a list of words
print(var1.count("F")) # counts the number of occurrences of "F" in the string
print(var1.capitalize()) # capitalizes the first letter of the string
print(var1.title()) # capitalizes the first letter of each word in the string
print(var1.replace("Farhad","Haseena")) # replaces "Farhad" with "Haseena" in the string
print(var1.endswith("!!!!!")) # checks if the string ends with "!!!!!"
print(var1.startswith("Haseena")) # checks if the string starts with "Farhad"
print(var1.find("rashid")) # finds the index of the first occurrence of "rashid" in the string
print(var1.index("rashid")) # finds the index of the first occurrence of "rashid" in the string
var2="Farhad rashid 123"
print(var2.isalnum()) # checks if the string is alphanumeric and returns True(if space is not between as well) if it is, otherwise False
print(var1.isalpha()) # checks if the string is alphabetic
str_numeric = "123456"
print(str_numeric.isdigit()) # checks if the string is numeric
print(var2.islower()) # checks if the string is in lowercase