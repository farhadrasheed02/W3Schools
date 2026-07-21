#Case: 1 Default Parameter: If we pass the value within the function as in this example, It is called default parameter function. these values can be overridden by
# passing the values while calling the function.
def calculateMean(a =2 , b =2):     # Function with default parameters
    result = (a * b) / (a + b)
    print("Default Arguments : ",result)

calculateMean(10) # here we are passing only one value, so the second value will be taken from the default parameter.


# Case: 2 Keyword Parameter: If we pass the value within the function as in this example,
# It is called keyword parameter function. these values can be overridden by


def calculateMean(a , b):     # Function with Required parameters if we don't pass the values while calling the function, it will throw an error.
    result = (a * b) / (a + b)
    print("Required Arguments : ",result)

calculateMean(10,5) #here we are passing both the values, otherwise it will throw an error(TypeError: calculateMean() missing 1 required positional argument: 'b').

def fName(fname,lname="Reshi"):
    return f"Hello {fname} {lname}"
print(fName("Farhad")) # here we are passing only one value, so the second value will be taken from the default parameter.
print(fName("Farhad","Khan")) # here we are passing both the values, so the second value will be overridden by the passed value.


def addition(a,b):
    return a+b
print(addition(a=10, b =5)) # here we are passing arguments with a key = value, so the order of the arguments doesn't matter.

def average(*args): # here we are passing a variable number of arguments, so we can pass any number of arguments while calling the function.
    print(type(args))
    return sum(args)/len(args)
print(average(10,20,30,40,50)) # here we are passing 5 arguments, but we can pass any number of arguments while calling the function.


def displayInfo(**kwargs): # here we are passing a variable number of keyword arguments, so we can pass any number of keyword arguments while calling the function.
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")
displayInfo(Name="Farhad", Age=25, City="New York") # here we are passing 3 keyword arguments, but we can pass any number of keyword arguments while calling the function
