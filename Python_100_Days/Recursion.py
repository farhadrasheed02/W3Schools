from Utilities.Input_file import user_input as user_input_value
from Utilities.Functions import factorial as fac


us_input = user_input_value() # Taking User Input from the Input_file
#Factorial Function getting implemented..
fact_value = fac(us_input) #Passing Factorial function the input from the user
print(f"Factorial  of {us_input} is :",fact_value)
print(fac.__doc__) #doc string getting used here. buddy

#Fibonacci Series
