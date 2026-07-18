from numpy.testing.print_coercion_tables import print_new_cast_table

string_var = 'He said , "I want to learn Python."'
print(string_var)

var_2 = "He said, \"I want to eat an apple \"" # string within double quotes is not allowed, so we need to use escape character
print(var_2)
var = "farhad "
print(var[::-1])
print(var.capitalize())
print(len(var))
for i in range(len(var)):
    print(var[i].capitalize())

# String Slicing
fruit = "banana ,apple, mango"
print(len(fruit))
print(fruit[0:3]) # prints 'ban'

name = "farhad"
print(name[-4:-1]) # prints 'rha'
print(name[2:5])