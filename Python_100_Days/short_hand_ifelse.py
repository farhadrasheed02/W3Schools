# a  = 20
# b = 30
# print("A") if (a>b) else print("B") if (a<b) else print("=")
user_input = int(input("Enter a number: "))
print("Even") if user_input % 2 == 0 else print("Odd")

print(f"The value is {user_input}")