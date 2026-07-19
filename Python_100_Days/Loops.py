# from Utilities.Logging_Report import logger
from Utilities import Logging_Report

# For Loop over a range of numbers
a = 20
for i in range(a+1):
    pass
    Logging_Report.logger.info(f"Current value of i: {i}")

# for Loop over the list
colors  = ["Red","Orange","Yellow","Green","Blue","Indigo","Violet"]
for color in colors:
    for i in color:
        Logging_Report.logger.info(f"Current character: {i} in color: {color}")

# While Loop
count = int(input("Enter a number: "))
while count <= 20:
    Logging_Report.logger.info(f"Current count: {count}")
    count += 2
print("While loop completed.")

# do While
count = int(input("Enter a number: "))
do:Logging_Report.logger.info(f"Current count: {count}")
count += 1
while count <= 20:
    Logging_Report.logger.info(f"Do While : {count}")
    count += 2