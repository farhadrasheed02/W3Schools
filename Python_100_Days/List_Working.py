marks = [85, 90, 78, 92, 88,"Farhad",True]  # we can add different data types in a list this is called heterogeneous list
print("Marks:", marks)
# print("Highest mark:", max(marks))
print(marks[3])
# print(marks[7])  #IndexError: list index out of range
if "Farhad" in marks:
    print("Farhad is present in the list")
marks.append(95)  # adding an element to the end of the list
print("Marks after appending:", marks)

# :: -1 means start:stop:step
print("Marks in reverse order:", marks[::-1])  # printing the list in reverse order
import array as arr
arr_1 = arr.array('i',(1, 2, 3, 4, 5))  # creating an array of integers
print(type(arr_1))  # printing the type of the array
print("Array:", arr_1)

