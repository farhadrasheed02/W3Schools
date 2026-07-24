tup_1 = 1 #similar to (1) and if we have to make it tuple, we have to add a comma after the value.
print(type(tup_1))  # Output: <class 'int'> Comma makes the tuple, not parentheses.
tup_2 = (1,)  # This is a tuple with one element
print(type(tup_2))  # Output: <class 'tuple'>
lst = [1]
print(type(lst))  # Output: <class 'list'>

tup = (1, 2, 3, 4, 5,"Farhad",True)  # This is a tuple with multiple elements
# Accessing elements in a tuple
print(tup[0])  # Output: 1
print(tup[5])  # Output: Farhad
# tup[0] = 10  #TypeError: 'tuple' object does not support item assignment
for i in tup:
    print(i)
tup_new = (i  for i in range(10))
for value in tup_new:
    print(value)
if 9 in tup_new:
    print("9 is present in the tuple")

