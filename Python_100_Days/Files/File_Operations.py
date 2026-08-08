f = open("test.txt", "a")
f.write("This is a test file. \n")
f.close()
f1 = open("test.txt", "r")
content = f1.read()
print(content)
f.close()




