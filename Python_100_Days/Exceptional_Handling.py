l = []
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


#get input and save in a list then raise different exceptional handling in it..
try:
    l = []
    for i in range(0,a):
        l.append(i)
        print(l[a+2])
except IndexError:
    print("Index Error")

finally:
    print("I am ")
