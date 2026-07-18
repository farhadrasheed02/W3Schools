a ="5"
b= "Farhad"
print(a+b) # 57
# TypeCasting (Explicit Conversion) str to int
a = int(a)
b = int(b) #Error: invalid literal for int() with base 10: 'Farhad' (because 'Farhad' cannot be converted to an integer as It is a string of characters)
print(a+b) # 12

# Implicit TypeCasting
a = 5.8
b = 2
print(a+b) # 7.8 (here b is converted to float implicitly to prevent data loss)