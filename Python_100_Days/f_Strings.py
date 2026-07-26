# Older way of formatting strings
letter = "My Name is {name} and I am {age} years old."
name = "Farhad"
Age = 30
print(letter.format(name=name, age=Age))

# f string will overcome with the previous formating introduced after Python 3.6 onwards

letter = f"My Name is {name} and I am {Age} years old"
print("F String involved :",letter)

price = 2.49876541
print(f"The price is {price : .2f} $")
