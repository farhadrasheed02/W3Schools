f1 = open("test.txt", "r")
while True:
    line =f1.readline()
    if not line:
        break
    print(line)

# f.write("This is a test file. \n")
#
# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)



