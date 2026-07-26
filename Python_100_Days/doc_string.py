from Utilities.Functions import square as sq
"""
What is written here in these quotes defines the doc string It actually allows the developer/visitors of the code to know
what actually the code is executing during the process...
"""

user_input= int(input("Enter the Number : "))
var = sq(user_input)
print(f"Square root of {user_input} is :",var)
print(sq.__doc__) # this is the way to print the ooc string of a function that shows what is happening in the backend during execution.
