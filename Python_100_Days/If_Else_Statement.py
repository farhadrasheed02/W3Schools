# vote Eligibility Checker
U_input = int(input("Enter the Age of the Person : "))
if U_input < 18:
    print("The Person is a Minor and is not eligible to vote.")
elif 18 <= U_input <= 30:
    print("The Person is a Young Adult and is eligible to vote.")
elif 30 < U_input <= 60:
    print("The Person is an Adult and is eligible to vote.")
else:
    print("The Person is a Senior Citizen and is eligible to vote.")

# Grade Checker
marks = int(input("Enter the Marks of the Student : "))
if marks == 100:
    print("The Student has received an A++ grade.")
elif 90 <= marks  < 100:
    print("The Student has received an A grade.")
elif 75 <= marks < 90:
    print("The Student has received a B Grade equals Distinction.")
elif 60 <= marks < 75:
    print("The Student has received a C grade.")
elif 50 <= marks < 60:
    print("The Student has received a D grade.")
elif 34 <= marks < 50:
    print("The Student has received an E grade.")
elif marks == 33:
    print("The Student has received a Survived grade for next exam.")
else:
    print("The Student has received an F grade and has failed the exam.")