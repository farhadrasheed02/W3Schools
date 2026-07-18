User_Input = input("Please enter your name: ")
print("Hello, " + User_Input + "! Welcome to the Python 100 Days challenge.")

# Remember input() function takes userinput as a string so we need to typecase the input before performing any mathematical operations.
# For example, if we want to add two numbers entered by the user, we need to convert the inputs to integers before adding them.
add_input = input("Enter the first number: ")
add_input2 = input("Enter the second number: ")
sum_result = (add_input) + (add_input2)
print("The sum of " + add_input + " and " + add_input2 + " is: " + str(sum_result)) #if i enter 5 and 10, it will print 510 instead of 15 because the inputs are treated as strings. To fix this, we need to convert the inputs to integers before adding them.

print("The sum of " + add_input + " and " + add_input2 + " is: " + str(int(add_input) + int(add_input2))) # This will correctly print the sum as an integer. because we have specified that the inputs should be converted to integers using the int() function before performing the addition.
