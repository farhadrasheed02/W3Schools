x = int(input("Enter a number: "))

match x:
    case x if 1 <= x <= 17:
        print("You have reached to an Age of Majority and you are eligible to vote.")
    case x if 18 <= x <= 29:
        print("You have reached to an Age of Maturity and you are eligible to apply for a driver's license.")
    case x if 30 <= x <= 100:
        print("You have reached to an Age of Adulthood and you are eligible to apply for a passport.")
    case _:
        print("You are not eligible for any of the above mentioned privileges.")
