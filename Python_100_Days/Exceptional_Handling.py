from pycparser.ply.cpp import literals

try:
    a = int(input("Enter the number: "))
    print(f"Multiplication Table of {a} is :")
except  Exception as exp:
    print("Please enter Integer only")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as exp:
    print("The Input must be Integer")

print("Some important Lines are getting executed post exception")
print("End of the programme")