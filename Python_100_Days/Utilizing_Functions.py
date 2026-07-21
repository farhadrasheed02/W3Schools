import Utilities.Functions as func
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

result = func.addition(num_1, num_2)
print(f"The sum of {num_1} and {num_2} is: {result}")


sub_result = func.subtraction(num_1, num_2)
print(f"The difference of {num_1} and {num_2} is: {sub_result}")

mult_result = func.multiplication(num_1, num_2)
print(f"The product of {num_1} and {num_2} is: {mult_result}")

div_result = func.division(num_1, num_2)
if div_result is not None:
    print(f"The division of {num_1} by {num_2} is: {div_result}")