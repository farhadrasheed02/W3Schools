var = str(input("Enter the string :"))


if len(var) >= 3:
    var1 = var[0] #removed first element
    var2 = var[1:] #string without the first element
    result_string = var2+var1 #combination of string without the first element and added removed element at the back.
    print(result_string)
elif len(var)<3:
    reverse_text = var[::-1]
    print("Reverse String "+reverse_text)
