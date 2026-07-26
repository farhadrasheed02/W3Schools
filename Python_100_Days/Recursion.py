from Utilities.Input_file import user_input as user_input_value
from Utilities import Functions as fun


us_input = user_input_value() # Taking User Input from the Input_file
#Factorial Function getting implemented.
fact_value = fun.factorial(us_input) #Passing Factorial function the input from the user
print(f"Factorial  of {us_input} is :",fact_value)
print(fun.factorial.__doc__) #doc string getting used here. buddy

#Fibonacci Series getting implemented...
Fib_Series = []
for i in range(us_input):
    Fib_Series.append(fun.Fibonacci(i))
print(f"Fibonacci Sequence for {us_input} is :",Fib_Series)
