import os

if not os.path.exists("Python Days"):
    os.mkdir("Python Days")
    print("Directory created successfully at "+ os.getcwd() + "/Python Days")
    for i in range(0,10):
        os.mkdir("Python Days/Day " + str(i+1))
        print("Directory created successfully at "+ os.getcwd() + "/Python Days/Day " + str(i+1))
else:
    print("Directory already exists at "+ os.getcwd() + "/Python Days")